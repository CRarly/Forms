<?php
$dbHost = 'https://databases-auth.000webhost.com/index.php?route=/table/operations&db=id18425865_db_dre_projetada&table=Usu%C3%A1rios';
$dbUsername = 'id18425865_controladoriaucb@2a02:4780:bad:c0de::14'
$dbPassword = '';
$dbName = 'id18425865_db_dre_projetada';

$conexao = new mysqli($dbHost, $dbUsername, $dbPassword, $dbName)

  if($conexao->connect_errno)
  {
    echo "Erro";
  }
  else
  {
    echo "Conexão efetuada com sucesso";
  }
?>
