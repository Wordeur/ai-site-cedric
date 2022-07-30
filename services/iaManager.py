import openai
import os

NEGATIF_MODEL="Genere moi un avis négatif intelligent pour la société d'electricien Inolys, société ce situant a Lille, écris par un client déçu"
POSITIF_MODEL="Genere moi un avis positif intelligent pour la société d'electricien Inolys ecris par un client satisfait\n"

class IaManager :
    'This is AI class for comunicate with GPT-3 IA' 
   
    # Une méthode utilisée pour créer l'objet (Contructor).
    def __init__(self):
        openai.api_key = os.getenv("AI_KEY")
   
    def generateReview(self, review_positif: bool):        
        model = POSITIF_MODEL

        if not review_positif:
            model = NEGATIF_MODEL

        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=model,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response.choices[0].text