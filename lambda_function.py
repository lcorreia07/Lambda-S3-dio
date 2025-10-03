import json

def lambda_handler(event, context):
    # Exemplo simples que só retorna o evento recebido
    print("Evento recebido:", json.dumps(event))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Função Lambda executada com sucesso!')
    }
