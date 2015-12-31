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
        <p><a class="btn btn-lg btn-success" href="#" role="button">Em breve!</a></p>
        </div>

        <div class="row">
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
