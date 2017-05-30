<?php

namespace Ewetasker\Performer;

/**
* 
*/
class MipPerformer
{
    private $mip_perfomer;
    
    function __construct()
    {
        return $this->mip;
    }

    function controlMip($parameter)
    {
        shell_exec('python ./performers/control_mip.py ' . $parameter);
    }
}
