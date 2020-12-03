import json

def loadJsonFile():
    jsonText = ''    
    with open("/home/moufdi/GitHubProjects/Projet_IHM_Multimodal/Projet_IHM_Multimodal/templates_file.json", "r") as templates_file:
        jsonText = templates_file.read()
        templates = json.loads(jsonText)
    return templates

def saveTemplate(templates,listFigurePoints,templateName):
    with open("/home/moufdi/Projet_IHM_Multimodal/Projet_IHM_Multimodal/templates_file.json", "w") as templates_file:
        templates.append((listFigurePoints,templateName))
        json.dump(templates,templates_file)