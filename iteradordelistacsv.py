import csv

archivo_entrada = 'MANO-DE-OBRA - Hoja1 .tsv'
archivo_salida = 'archivo_salida.html'

with open(archivo_entrada, 'r', newline='', encoding='utf-8') as entrada:
    lector_tsv = csv.reader(entrada, delimiter='\t')
    datos = list(lector_tsv)

html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-alpha1/dist/css/bootstrap.min.css">
    <style>
    .preciolista{
    
    }
        #tabla-container {
            max-height: 300px;  /* Altura máxima del contenedor */
            overflow-y: scroll;  /* Habilitar el desplazamiento vertical */
        }
        .hidden {
            display: none;
        }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        function toggleContenido() {
            var contenido = document.getElementById('contenido');
            var boton = document.getElementById('boton-toggle');

            if (contenido.classList.contains('hidden')) {
                contenido.classList.remove('hidden');
                boton.textContent = 'OCULTAR LISTA';
            } else {
                contenido.classList.add('hidden');
                boton.textContent = 'BUSCAR EN LISTA CONS.M2';
            }
        }
        
        function buscar() {
            var input = document.getElementById('busqueda');
            var filter = input.value.toUpperCase();
            var table = document.getElementById('tabla');
            var rows = table.getElementsByTagName('tr');

            for (var i = 0; i < rows.length; i++) {
                var cell = rows[i].getElementsByTagName('td')[0];
                if (cell) {
                    var textValue = cell.textContent || cell.innerText;
                    if (textValue.toUpperCase().includes(filter)) {
                        rows[i].style.display = '';
                    } else {
                        rows[i].style.display = 'none';
                    }
                }
            }
        }
        
        function seleccionar(fila) {
            var nombreTarea = fila.cells[0].innerText;
            var precio = fila.cells[1].innerText;
            document.getElementById('nombre-tarea').value = nombreTarea;
            document.getElementById('precio').value = precio;
        }
    </script>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col">
                <button id="boton-toggle" class="btn btn-primary" onclick="toggleContenido()">BUSCAR EN LISTA CONS.M2</button>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div id="contenido" class="hidden">
                    <input type="text" id="busqueda" onkeyup="buscar()" class="form-control" placeholder="Buscar...">
                    <div id="tabla-container">
                        <table id="tabla" class="table table-striped">
                            <thead>
                                <tr>
                                    <th>Primera Columna</th>
                                    <th>Segunda Columna</th>
                                </tr>
                            </thead>
                            <tbody>
'''

for fila in datos:
    html += '<tr onclick="seleccionar(this)"><td>{}</td><td class="preciolista">{}</td></tr>\n'.format(fila[0], fila[1])

html += '''
                            </tbody>
                        </table>
                    </div>
                    <input type="text" id="nombre-tarea" readonly class="form-control">
                    <input type="text" id="precio" readonly class="form-control">
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

with open(archivo_salida, 'w', encoding='utf-8') as salida:
    salida.write(html)

print("Archivo HTML generado correctamente.")
