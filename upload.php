<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>A model template</title>
<link href="layout.css" rel="stylesheet" type="text/css" />
<meta name="Keywords" content="mol2 file" />
<meta name="author" content"Junjie Wang"/>
<meta name="Description" content="A model template" />
</head>

<body>
<div id="container">
  <div id="header">Efpdb.org</div>
  <div id="mainContent">

<!--Upload.php content-->
<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$input_charge = intval($_POST["charge"]);
//Get the upload file information
$fileinfo = pathinfo($target_file);
//Get the upload file type
$filetype = $fileinfo['extension'];
echo "Filetype is $filetype.\n<br \>";
if(isset($_POST["submit"])) {
    $check = filesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        echo "File is valid - " . $check["mime"] . ".\n<br />";
        $uploadOk = 1;
    } else {
        echo "File is not valid.\n<br />";
        $uploadOk = 0;
    }
}
// Check if file size is less than 20MB
if ($_FILES["fileToUpload"]["size"] > 20000000) {
    echo "Sorry, your file size cannnot exceed 20MB.\n<br />";
    $uploadOk = 0;
}
// Check if file is a xyz format
if($filetype !="xyz"){
    echo "The uploaded file is: \n<br \>".basename($_FILES["fileToUpload"]["name"])."\n<br />\n<br />";
    echo "Sorry, only .xyz file is allowed.\n<br />";
    $uploadOk=0;
}

//Check if there is an error
if($uploadOk == 0){
    echo "Sorry,your file was not uploaded.\n<br />";
}else{
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.\n<br />";
        //$output = system('/Applications/XAMPP/xamppfiles/htdocs/chemsimilarity.py $_FILES["fileToUpload"]["name"]');
        echo "Result from the chemsimilarity.py...<br />";
        $uploaded_file = $target_file;
        $output = exec("python searchstring.py $uploaded_file $input_charge");
        echo($output);
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
?>
<!--end of upload.php-->

</div>
  <div id="footer">This is the footer</div>
</div>
</body>
</html>
