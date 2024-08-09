from flask import Flask, jsonify, request

app = Flask(__name__)

def metros_a_yarda(metros):
    calculo = metros * 1.09361
    return calculo

def yarda_a_metros(yarda):
    calculo = yarda /1.09361
    return calculo
   
def pie_a_metros(pie):
    calculo = pie / 3.281
    return calculo

def metros_a_pie(metros):
    calculo = metros * 3.281
    return calculo
 
@app.route('/convertir', methods = ['POST'])
def convertir_longitud():
    data = request.get_json()
    input_medida=data.get('medida')
    
    if data['type_de'] == 'metros' and  data['type_a'] == 'yarda':
        result = metros_a_yarda(input_medida)
        output_unit = 'yarda'
    
    if data['type_de'] == 'yarda' and data['type_a'] == 'metros':
        result = yarda_a_metros(input_medida)
        output_unit = 'metros'
       
    if data['type_de'] == 'pie' and  data['type_a'] == 'metros':
        result = pie_a_metros(input_medida)
        output_unit = 'metros'
    
    if data['type_de'] == 'metros' and data['type_a'] == 'pie':
        result = metros_a_pie(input_medida)
        output_unit = 'pie'   
    return jsonify({"longitud": result, "unidad": output_unit})

if __name__ == '__main__':
    app.run(debug=False)