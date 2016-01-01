#html definitions

#defines start
HTML_HEADER = '''
<!DOCTYPE html>
<html lang='pt'>
    <head> <title>Lista de Restaurantes</title>
    <link href="css/bootstrap.css' rel='stylesheet'>
</head>
'''
#defines content

RESTAURANT_LAYOUT ='''
<body>
    <div class="container">
        <div class="jumbotron">
            <h1>Lista de Restaurantes</h1>
        <p class="lead"></p>
        <p><a class="btn btn-lg btn-success" href="restaurantOrdered" role="button">Ordenar por nome</a></p>
        <p><a class="btn btn-lg btn-success" href="new" role="button">Adicionar novo</a></p>
        </div>

        <div class="row">
'''

RESTAURANT_NEW ='''
        <div class="col-sm-12 col-md-9">
            <h1>Adi&ccedil&atildeo de Restaurante</h1>
                <form method='POST' enctype='multipart/form-data' action='/new'>
                    <h2>What's the name of the restaurant?</h2>
                    <input name="restaurant-new" type="text" ><input type="submit" value="Submit"></form>
        '''

RESTAURANT_EDIT ='''
        <div class="col-sm-12 col-md-9">
            <h1>Edi&ccedil&atildeo de restaurante</h1>
'''
RESTAURANT_EDIT_FORM = '''
<form method='POST' enctype='multipart/form-data'>
    <h2>What's the name of the restaurant?</h2>
    <input name="restaurant-edit" type="text" ><input type="submit" value="Submit"></form>
'''


RESTAURANT_TABLE ='''
           <div class="col-sm-12 col-md-9" id="restaurant_table">
                <table id="table-wrapper">
                    <thead>
                           <th>id</th>

                           <th class="acc-name">Restaurant name</th>
                           <th> Edit</th>
                           <th> Delete</th>
                    </thead>
                    <tbody>
'''
RESTAURNANT_TABLE_F='''
                    </tbody>
                </table>
                </div>
'''
RESTAURANT_LAYTOUT_E='''
            </div>
        </div>
'''
#defines page closer
PAGE_CLOSER ='''
    </body>
    </html>
'''
