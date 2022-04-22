
//SQL VM Parameters

param virtualMachineName string
param virtualMachineSize string = 'Standard_D2s_v3'

@allowed([
  'sql2019-ws2019'
  'sql2017-ws2019'
  'SQL2017-WS2016'
  'SQL2016SP1-WS2016'
  'SQL2016SP2-WS2016'
  'SQL2014SP3-WS2012R2'
  'SQL2014SP2-WS2012R2'
])
param imageOffer string = 'sql2019-ws2019'

@allowed([
  'Standard'
  'Enterprise'
  'SQLDEV'
  'Web'
  'Express'
])
param sqlSku string = 'Standard'

@allowed([
  'AHUB'
  'DR'
  'PAYG'
])
param sqlServerLicenseType string = 'PAYG'

param adminUsername string

@secure()
param adminPassword string

@description('SQL Server Workload Type')
@allowed([
  'DW'
  'GENERAL'
  'OLTP'
])
param storageWorkloadType string = 'GENERAL'

@description('Amount of data disks (1TB each) for SQL Data files')
@minValue(1)
@maxValue(8)
param sqlDataDisksCount int = 1

@description('Path for SQL Data files. Please choose drive letter from F to Z, and other drives from A to E are reserved for system')
param dataPath string = 'F:\\SQLData'

@description('Amount of data disks (1TB each) for SQL Log files')
@minValue(1)
@maxValue(8)
param sqlLogDisksCount int = 1

@description('Path for SQL Log files. Please choose drive letter from F to Z and different than the one used for SQL data. Drive letter from A to E are reserved for system')
param logPath string = 'G:\\SQLLog'
param location string = resourceGroup().location

// Existing Network Parameters
param sNetname  string
param vnetName string
param vnetRg string


var networkInterfaceName_var = 'nic-${virtualMachineName}-01'


var diskConfigurationType = 'NEW'
var dataDisksLuns = array(range(0, sqlDataDisksCount))
var logDisksLuns = array(range(sqlDataDisksCount, sqlLogDisksCount))
var dataDisks = {
  createOption: 'Empty'
  caching: 'ReadOnly'
  writeAcceleratorEnabled: false
  storageAccountType: 'Premium_LRS'
  diskSizeGB: 1023
}
var tempDbPath = 'D:\\SQLTemp'


resource vNet_external 'Microsoft.Network/virtualNetworks@2020-11-01' existing = {
  name: vnetName
  scope: resourceGroup(vnetRg)
}

resource networkInterfaceName 'Microsoft.Network/networkInterfaces@2020-06-01' = {
  name: networkInterfaceName_var
  location: location
  properties: {
    ipConfigurations: [
      {
        name: 'ipconfig1'
        properties: {
          subnet: {
            id: '${vNet_external.id}/subnets/${sNetname}'
          }          
        }
      }
    ]
    enableAcceleratedNetworking: true
  }
}

resource virtualMachineName_resource 'Microsoft.Compute/virtualMachines@2020-06-01' = {
  name: virtualMachineName
  location: location
  properties: {
    hardwareProfile: {
      vmSize: virtualMachineSize
    }
    storageProfile: {
      osDisk: {
        createOption: 'FromImage'
        managedDisk: {
          storageAccountType: 'Premium_LRS'
        }
      }
      imageReference: {
        publisher: 'MicrosoftSQLServer'
        offer: imageOffer
        sku: sqlSku
        version: 'latest'
      }
      dataDisks: [for i in range(0, (sqlDataDisksCount + sqlLogDisksCount)): {
        lun: i
        createOption: dataDisks.createOption
        caching: ((i >= sqlDataDisksCount) ? 'None' : dataDisks.caching)
        writeAcceleratorEnabled: dataDisks.writeAcceleratorEnabled
        diskSizeGB: dataDisks.diskSizeGB
        managedDisk: {
          storageAccountType: dataDisks.storageAccountType
        }
      }]
    }
    networkProfile: {
      networkInterfaces: [
        {
          id: networkInterfaceName.id
        }
      ]
    }
    osProfile: {
      computerName: virtualMachineName
      adminUsername: adminUsername
      adminPassword: adminPassword
      windowsConfiguration: {
        enableAutomaticUpdates: true
        provisionVMAgent: true
      }
    }
  }
}

resource Microsoft_SqlVirtualMachine_SqlVirtualMachines_virtualMachineName 'Microsoft.SqlVirtualMachine/SqlVirtualMachines@2017-03-01-preview' = {
  name: virtualMachineName
  location: location
  properties: {
    virtualMachineResourceId: virtualMachineName_resource.id
    sqlManagement: 'Full'
    sqlServerLicenseType: sqlServerLicenseType
    storageConfigurationSettings: {
      diskConfigurationType: diskConfigurationType
      storageWorkloadType: storageWorkloadType
      sqlDataSettings: {
        luns: dataDisksLuns
        defaultFilePath: dataPath
      }
      sqlLogSettings: {
        luns: logDisksLuns
        defaultFilePath: logPath
      }
      sqlTempDbSettings: {
        defaultFilePath: tempDbPath
      }
    }
  }
}

output adminUsername string = adminUsername
