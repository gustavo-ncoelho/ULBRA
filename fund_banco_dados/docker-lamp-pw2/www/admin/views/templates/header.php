<!DOCTYPE html>
<html lang="pt-br">
<head>
    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <!-- jQuery -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
    <!-- Meu script e style -->
    <link rel="stylesheet" href="assets/css/style.css">
    <script src="assets/js/script.js"></script>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel Administrativo</title>
</head>
<body>
    <header class="p-5 text-black text-center header-admin">
        <h1>Área Administrativa do Sistema</h1>
    </header>

    <div class="container-fluid header-nav-admin">
        <div class="row h-50">
            <nav class="col-md-3 header-admin-nav text-white">
                <h2>Menu</h2>
                <ul class="nav flex-column">
                    <li class="nav-item">
                        <a class="nav-link text-white" href="?controller=main&action=index" id="menuAdminHome">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href="?controller=client&action=listClients">Clientes</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href='http://localhost/admin/?controller=UserController&action=logout' id="menuAdminLogout">Sair</a>
                    </li>
                </ul>
                <h2>Clientes</h2>
				<ul class="nav flex-column">
					<li class="nav-item">
						<a class="nav-link" href="?controller=client&action=listClients">Listar</a>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="?controller=client&action=insertClient">Inserir</a>
					</li>
				</ul>
            </nav>
            <section class="col-md-9">