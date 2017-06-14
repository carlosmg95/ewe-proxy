<?php

namespace Ewetasker\Performer;

/**
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
        shell_exec('python ./performers/control_mip.py ' . $parameter);
    }
}
