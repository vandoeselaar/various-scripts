<?php

function get_data($url)
{
  $ch = curl_init();
  $timeout = 5;
  curl_setopt($ch,CURLOPT_URL,$url);
  curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
  curl_setopt($ch,CURLOPT_CONNECTTIMEOUT,$timeout);
  $data = curl_exec($ch);
  curl_close($ch);
  return $data;
}

if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
  $ip = $_SERVER['HTTP_CLIENT_IP'];
} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
} else {
    $ip = $_SERVER['REMOTE_ADDR'];
}

// niet ip maar locatie opslaan
// http://ip-api.com/json/24.48.0.1
$locatieDATA = get_data('http://ip-api.com/json/'.$ip);

$locatieJSON = json_decode($locatieDATA);
$locatie = (!empty($locatieJSON->city)) ? $locatieJSON->city : 'onbekend';

print_r($locatie);
?>