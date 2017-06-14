<?php

namespace Ewetasker\Performer;

/**
* shell_exec('python ./performers/control_mip.py ' . $parameter);
*/
class MipPerformer
{
    
    function __construct()
    {
        return $this->mip;
    }

    function controlMip($parameter)
    {
    	$orden = system( "python ./performers/control_mip.py $parameter" ); 
    	return;
    }
}
