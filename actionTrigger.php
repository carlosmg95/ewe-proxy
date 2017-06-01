<?php

use Ewetasker\Performer\ChromecastPerformer;
use Ewetasker\Performer\HueLightPerformer;
use Ewetasker\Performer\ApiaiPerformer;
use Ewetasker\Performer\MipPerformer;

include_once('./performers/chromecastPerformer.php');
include_once('./performers/hueLightPerformer.php');
include_once('./performers/apiAiPerformer.php');
include_once('./performers/mipPerformer.php');

$actions = isset($_POST['actions']) ? $_POST['actions'] : [];

if (isset($_POST['channel']) && isset($_POST['action'])) {
    $action = array();
    $action['channel'] = $_POST['channel'];
    $action['action'] = $_POST['action'];
    $action['parameter'] = isset($_POST['parameter']) ? $_POST['parameter'] : "";
    array_push($actions, $action);
}

foreach ($actions as $action) {
    echo $action;
    echo $action['channel'];
    echo $action['action'];
    switch ($action['channel']) {
        case 'Chromecast':
            $chromecast = new ChromecastPerformer();
            switch ($action['action']) {
                case 'PlayVideo':
                    $chromecast->playVideo($action['parameter']);
                    break;
                
                default:
                    # code...
                    break;
            }
            unset($chromecast);
            break;

        case 'HueLight':
            $huelight = new HueLightPerformer();
            switch ($action['action']) {
                case 'TurnOn':
                    $huelight->turnOn();
                    break;
                case 'TurnOff':
                    $huelight->turnOff();
                    break;
                case 'SetBrightness':
                    $huelight->setBrightness($action['parameter']);
                    break;
                
                default:
                    # code...
                    break;
            }
            unset($huelight);
            break;
         case 'apiai':
            $apiai = new ApiaiPerformer();
            switch ($action['action']) {
                case 'Send event':
                    $apiai->sendEvent($action['parameter']);
                    break;
                
                default:
                    # code...
                    break;
            }
            unset($huelight);
            break;
        case 'RobotMip':
            $mip = new MipPerformer();
            switch ($action['action']) {
                case 'ControlRobot':
                    $mip->controlMip($action['parameter']);
                    break;
                
                default:
                    # code...
                    break;
            }
            unset($mip);
            break;
        default:
            # code...
            break;
    }
}
