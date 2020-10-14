<?php
function formataCPF($str) {
    $temp = str_replace('.', '', $str);
    $temp = str_replace('-', '', $temp);

    $temp = substr($temp, 0, 3).'.'.substr($temp, 3, 3).'.'.substr($temp, 6, 3).'-'.substr($temp, 9, 2);

    return $temp;
}

function formataCNPJ($str) {
    $temp = str_replace('.', '', $str);
    $temp = str_replace('-', '', $temp);
    $temp = str_replace('/', '', $temp);

    $temp = substr($temp, 0, 2).'.'.substr($temp, 2, 3).'.'.substr($temp, 5, 3).'/'.substr($temp, 8, 4).'-'.substr($temp, 12, 2);

    return $temp;
}

function formataRG($str){
    $temp = str_replace('.', '', $str);
    $temp = str_replace('-', '', $temp);

    $temp = substr($temp, 0, -1).'-'.substr($temp, -1);

    return $temp;
}

function formataCEP($str) {
    $temp = str_replace('-', '', $str);
    $temp = substr($temp, 0, -3).'-'.substr($temp, -3);
    return $temp;
}

error_reporting(E_ERROR | E_PARSE);
require_once('database.php');

header('Content-Type: text/csv');
header('Content-Disposition: attachment; filename="mage1_customer.csv"');

$csvHeader = 'Name,VAT/TAX,SSN,EIN,EI,Date of birth,Gender,Street,Street number,Complement,Neighborhood,City,State,Zip,Phone Prefix,Phone,Mobile Prefix,Mobile,Commercial Prefix,Commercial,Email';
$csv = Array();
array_push($csv, $csvHeader);

$sql = "
    SELECT 
        customer_entity.email,
        first_name.value AS name,
        last_name.value AS surname,
        address_street.value AS street,
        address_city.value AS city,
        address_postcode.value AS zip,
        address_region.value AS state,
        vat.value AS vat,
        rg.value AS SSN,
        dob.value AS dob,
        gender.value AS gender,
        phone.value AS phone,
        mobile.value AS mobile
    FROM 
        customer_entity
    JOIN 
        customer_entity_varchar AS first_name 
    ON 
        customer_entity.entity_id = first_name.entity_id
    JOIN 
        customer_entity_varchar AS vat 
    ON 
        customer_entity.entity_id = vat.entity_id
    JOIN 
        customer_entity_datetime AS dob 
    ON 
        customer_entity.entity_id = dob.entity_id
    JOIN 
        customer_entity_varchar AS rg 
    ON 
        customer_entity.entity_id = rg.entity_id
    JOIN 
        customer_entity_int AS gender 
    ON 
        customer_entity.entity_id = gender.entity_id
    JOIN 
        customer_entity_varchar AS last_name 
    ON 
        customer_entity.entity_id = last_name.entity_id
    JOIN 
        customer_address_entity AS address_address 
    ON 
        customer_entity.entity_id = address_address.parent_id
    JOIN 
        customer_address_entity_varchar AS address_first_name 
    ON 
        address_address.entity_id = address_first_name.entity_id
    JOIN 
        customer_address_entity_varchar AS address_last_name 
    ON 
        address_address.entity_id = address_last_name.entity_id
    JOIN 
        customer_address_entity_text AS address_street 
    ON 
        address_address.entity_id = address_street.entity_id
    JOIN 
        customer_address_entity_varchar AS address_city 
    ON 
        address_address.entity_id = address_city.entity_id
    JOIN 
        customer_address_entity_varchar AS address_postcode 
    ON 
        address_address.entity_id = address_postcode.entity_id
    JOIN 
        customer_address_entity_varchar AS address_region 
    ON 
        address_address.entity_id = address_region.entity_id
    JOIN 
        customer_address_entity_varchar AS phone 
    ON 
        address_address.entity_id = phone.entity_id
    JOIN 
        customer_address_entity_varchar AS mobile 
    ON 
        address_address.entity_id = mobile.entity_id
    WHERE 
        first_name.entity_type_id = 1
    AND 
        first_name.attribute_id = 5
    AND 
        last_name.entity_type_id = 1
    AND 
        last_name.attribute_id = 7
    AND 
        address_first_name.entity_type_id = 2
    AND 
        address_first_name.attribute_id = 20
    AND 
        address_last_name.entity_type_id = 2
    AND 
        address_last_name.attribute_id = 22
    AND 
        address_street.entity_type_id = 2
    AND 
        address_street.attribute_id = 25
    AND 
        address_city.entity_type_id = 2
    AND 
        address_city.attribute_id = 26
    AND 
        address_postcode.entity_type_id = 2
    AND 
        address_postcode.attribute_id = 30
    AND 
        address_region.entity_type_id = 2
    AND 
        address_region.attribute_id = 28
    AND 
        vat.entity_type_id = 1
    AND 
        vat.attribute_id = 15
    AND 
        rg.entity_type_id = 1
    AND 
        rg.attribute_id = 146
    AND 
        dob.entity_type_id = 1
    AND 
        dob.attribute_id = 11
    AND 
        gender.entity_type_id = 1
    AND 
        gender.attribute_id = 18
    AND 
        phone.entity_type_id = 2
    AND 
        phone.attribute_id = 31
    AND 
        mobile.entity_type_id = 2
    AND 
        mobile.attribute_id = 32";
$result = mysqli_query($CONN, $sql);

while($row = mysqli_fetch_assoc($result)) {
    /*
        Split the address in parts
        0 - Number
        1 - Street
        2 - Complement
        3 - neighborhood
    */
    $streetArray = explode("\n", $row['street']);

    $fullName = $row['name'].' '.$row['surname'];

    $vat = str_replace('.', '', $row['vat']);
    $vat = str_replace('-', '', $vat);
    
    if(strlen($cpf) > 11) {
        $cpf = "";
        $cnpj = formataCNPJ($cpf);
    } else {
        $cpf = formataCPF($cpf);
        $cnpj = '';
    }
    
    $SSN = str_replace('.', '', $row['SSN']);
    $SSN = str_replace('-', '', $SSN);
    if(strlen($SSN) >= 9)
        $SSN = formataRG($SSN);
    else
        $SSN = '';

    $EI = '';
    $dob = date('Y-m-d', strtotime($row['dob']));

    switch($row['gender']) {
        case "1":
            $gender = 'Male';
        break;
        case "2":
            $gender = 'Female';
        break;
        default: 
            $gender = 'Other';
        break;
    }

    $street = $streetArray[1];
    $numero = $streetArray[0];

    if(count($streetArray) < 4) {
        $bairro = $streetArray[2];
        $complemento = '';
    } else if (count($streetArray) == 4){    
        $total = count($streetArray);
        $bairro = $streetArray[$total - 1];
        for($i = 2; $i < $total-1; $i++) {
            $complemento .= $streetArray[$i].' ';
        }
    }
    $complemento = str_replace(',', ' ', $complemento);

    $street = str_replace(',', ' - ', $street);
    $number = str_replace(',', ' - ', $number);
    $neighborhood = str_replace(',', ' - ', $neighborhood);

    $city = $row['city'];
    $state = $row['state'];
    $zip = formataCEP($row['zip']);
    $prefixPhone = substr($row['phone'], 1, 2);
    $phone = substr($row['phone'], 5, 9);
    $prefixMobile = substr($row['mobile'], 1, 2);
    $mobile = substr($row['mobile'], 5, 10);
    $prefixCommercial = '';
    $commercial = '';
    $email = $row['email'];

    $csvRow = "$fullName,$vat,$SSN,$cnpj,$EI,$dob,$gender,$street,$number,$complemento,$neighborhood,$city,$state,$zip,$prefixPhone,$phone,$prefixMobile,$mobile,$prefixCommercial,$commercial,$email";  
    array_push($csv, $csvRow);
    $fullName='';
    $vat='';
    $SSN='';
    $cnpj='';
    $EI='';
    $dob='';
    $gender='';
    $street='';
    $number='';
    $complemento='';
    $neighborhood='';
    $city='';
    $state='';
    $zip='';
    $prefixPhone='';
    $phone='';
    $prefixMobile='';
    $mobile='';
    $prefixCommercial='';
    $commercial='';
    $email='';
}

$fp = fopen('php://output', 'wb');
foreach ( $csv as $line ) {
    $val = explode(",", $line);
    fputcsv($fp, $val);
}
fclose($fp);

?>