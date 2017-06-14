<?php

namespace Ewetasker\Performer;

/**
*system( "python ./performers/control_mip.py $parameter >>out.txt 2>>error.txt &" );
*  
*/
class MipPerformer
{
    
    function __construct()
    {
        return $this->mip;
    }

    function controlMip($parameter)
    {
    	ob_end_clean();
		header("Connection: close");
		ob_start();
		echo ('Response Sent');
		$size = ob_get_length();
		header("Content-Length: $size");
		ob_end_flush(); // Strange behaviour, will not work
		flush();            // Unless both are called !
		// Do processing here
    	shell_exec('python ./performers/control_mip.py ' . $parameter);
    }
}
