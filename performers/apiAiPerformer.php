<?php

namespace Ewetasker\Performer;

/**
* 
*/
class ApiaiPerformer
{
    private $apiai_performer;
    
    function __construct()
    {
        return $this->apiai_performer;
    }

    function sendEvent($message)
    {
		$url = "https://api.api.ai/api/query?v=20150910";
        $sessionId = '1234';
		$data = array('text'=>$message );
		$event = array('name'=> 'event_reminder', 'data'=>$data);
		$data_send = array("event" => $event,'timezone'=>'Europe/Madrid', 'lang'=>'en', 'sessionId'=>$sessionId);     
		$data_string = json_encode($data_send);  
		print_r("DENTRO DEL PERFORMER");
		$curl = curl_init($url);
		curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "POST");                                                                     
		curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);                                                                  
		curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);                                                                      
		curl_setopt($curl, CURLOPT_HTTPHEADER, array(                                                                          
		    'Content-Type: application/json; charset=utf-8','Authorization: Bearer a6b0be7a8a1247e69c8acbd8e7e1aaaf')                                                                       
		    );                                                                                                                   
		$result = curl_exec($curl);
		print_r($result);
    }
}
