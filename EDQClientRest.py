from DevBase import DevBase
import config
class EDQClientRest(DevBase):
    def __init__(self):
        super().__init__(self)

    def _create_job(self,job_name):

        """Creation of Job with request body
            with datasetId and job Name
        
        """
        params = {'datasetConfigurationId':config.default_config.datasets[config.default_config.datasets.keys()[0]],
                  'job_name':job_name}
        json_response = self._create_job_configuration(params)
        return {"status":f"Job ID created: {json_response['jobId']}"}
    

    def _create_dataset(self,file_list):
        
        """creating dataset
        
        """
        params = {'filelist':file_list}
        json_response = self._create_dataset(params)
        return {"status":f"DataSet ID created: {json_response['datasetConfigurationId']}"}
    

    def _create_rulesetId(self,name):
        """
        create ruleset and get the ruleset Id
        """
        #YTD input params
        params = {"rulesetName":name} 
        json_response = self._create_rule_set(params)
        return {"status":f"RuleSet ID created: {json_response['rulesetId']}"}
    
    def _check_for_rule_exists(self,ruleId):
        params = {'datasetConfigurationId':config.default_config.datasets[config.default_config.datasets.keys()[0]]}
        rules = self._check_for_rule_exists(params)
        if ruleId in rules:
            return True
        else:
            return False
        
    def _create_rule(self,**kwargs):
        """
        creation of rules and attaching rules to ruleset
        
        """
      
        json_response = self._create_rule(kwargs)
        return {"status":f"Rule IDcreated: {json_response['jobId']}"}
    
    def _schedule_job(self,jobId):
        """
        Job Schedule based on Job  Id
        
        """
        params = {'datasetConfigurationId':config.default_config.datasets[config.default_config.datasets.keys()[0]],
                  'jobId':jobId}
        json_response = self._schedule_job(params)
        return {"status":f"Job ID created: {json_response['jobId']}"}
    
