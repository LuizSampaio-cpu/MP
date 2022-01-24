import PyPDF2
import textract
import json
import nltk
import matplotlib.pyplot as plt

# Observações:
# 1) Apesar de apresentar alguns avisos, o programa roda normalmente;
# 2) Por não conseguir otimizar o tamanho, o programa demora um certo tempo para executar tudo;
# 3) ALgumas das bibliotecas importadas neste programa necessitam de instalação via pip install no prompt de comando do computador para que funcionem do jeito correto; 


def busca(pdf):
    x = 0
    lista = []
    chave = [
        "RDF", "Protege", "OWL", "ITU", "ISO", "TMFORUM", "DMTF", "IETF",
        "F-LOGIC", "RDFS", "CIM", "Accounting", "fault", "performance",
        "Security", "configuration"
    ]
    for i in range(len(chave)):
        lista.append(pdf.count(chave[x]))
        x = x + 1
    
    return lista


nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def pdfRead(arquivo):

    pdfFileObj = open(arquivo, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    num_pages = pdfReader.numPages

    count = 0
    text = ""

    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()

    if text != "":
        text = text
    else:
        text = textract.process(fileurl, method='tesseract', language='eng')

    tokens = word_tokenize(text)

    punctuations = ['(', ')', ';', ':', '[', ']', ',']

    stop_words = stopwords.words('english')

    keywords = [
        word for word in tokens
        if not word in stop_words and not word in punctuations
    ]

    return keywords


def geraGrafico(lista):

    with open("keywords.json", "rb") as f:
        termos = json.load(f)
        labels = termos["termos"]

        sizes = lista

        fig1, ax1 = plt.subplots()

        ax1.pie(sizes,
                labels=labels,
                autopct='%1.1f%%',
                shadow=True,
                startangle=90)
        ax1.axis('equal')

        plt.show()


def main():
    listaFinal = []
    i = 0
    arquivo1 = pdfRead(
        "A comprehensive semantic-based resource allocation framework for workflow management systems.pdf"
    )
    lista1 = busca(arquivo1)

    arquivo2 = pdfRead(
        "A framework for modeling and reasoning about network management resources and services to support information reuse.pdf"
    )
    lista2 = busca(arquivo2)

    arquivo3 = pdfRead(
        "A multi-layered agent ontology system for resource inventory.pdf")
    lista3 = busca(arquivo3)

    arquivo4 = pdfRead(
        "A semantic approach to evaluate the impact of cyber actions on the physical domain.pdf"
    )
    lista4 = busca(arquivo4)

    arquivo5 = pdfRead(
        "A semantic model for enhancing network services management and auditing.pdf"
    )
    lista5 = busca(arquivo5)

    arquivo6 = pdfRead(
        "A study in the expressiveness of semantically different policy modelling schemes.pdf"
    )
    lista6 = busca(arquivo6)

    arquivo7 = pdfRead(
        "An ontology-based approach for semantic interoperability in interorganizational IT service management.pdf"
    )
    lista7 = busca(arquivo7)

    arquivo8 = pdfRead(
        "An ontology-based approach to the description and execution of composite network management processes for network monitoring.pdf"
    )
    lista8 = busca(arquivo8)

    arquivo9 = pdfRead(
        "An Ontology-Based Information Extraction System for bridging the configuration gap in hybrid SDN environments.pdf"
    )
    lista9 = busca(arquivo9)

    arquivo10 = pdfRead(
        "Application of OWL-S to define management interfaces based on Web services.pdf"
    )
    lista10 = busca(arquivo10)

    arquivo11 = pdfRead(
        "Composing user network operation services using Web service composition techniques.pdf"
    )
    lista11 = busca(arquivo11)

    arquivo12 = pdfRead(
        "Enhancing Event Processing Networks with semantics to enable self-managed SEE federations.pdf"
    )
    lista12 = busca(arquivo12)

    arquivo13 = pdfRead(
        "ENM_ A service oriented architecture for ontology-driven network management in heterogeneous network infrastructures.pdf"
    )
    lista13 = busca(arquivo13)
    arquivo14 = pdfRead(
        "Implementation and application of a well-founded configuration management ontology.pdf"
    )
    lista14 = busca(arquivo14)

    arquivo15 = pdfRead(
        "Integrating heterogeneous IT_network management models using linked data.pdf"
    )
    lista15 = busca(arquivo15)

    arquivo16 = pdfRead(
        "Multi-domain fault management architecture based on a Shared ontology-based Knowledge Plane.pdf"
    )
    lista16 = busca(arquivo16)

    arquivo17 = pdfRead(
        "Network access control configuration management using semantic web techniques.pdf"
    )
    lista17 = busca(arquivo17)

    arquivo18 = pdfRead(
        "New developments in ontology-based policy management- Increasing the practicality and comprehensiveness of KAoS.pdf"
    )
    lista18 = busca(arquivo18)

    arquivo19 = pdfRead(
        "Ontological configuration management for wireless mesh routers.pdf")
    lista19 = busca(arquivo19)

    arquivo20 = pdfRead(
        "Ontological semantics for distributing contextual knowledge in highly distributed autonomic systems.pdf"
    )
    lista20 = busca(arquivo20)

    arquivo21 = pdfRead(
        "Ontology-based information extraction from the configuration command line of network routers.pdf"
    )
    lista21 = busca(arquivo21)

    arquivo22 = pdfRead(
        "Ontology-based policy refinement using SWRL rules for management information definitions in OWL.pdf"
    )
    lista22 = busca(arquivo22)

    arquivo23 = pdfRead("Ontology-based policy translation.pdf")
    lista23 = busca(arquivo23)

    arquivo24 = pdfRead(
        "Ontology-driven automatic construction of bayesian networks for telecommunication network management.pdf"
    )
    lista24 = busca(arquivo24)

    arquivo25 = pdfRead(
        "Resolving tactical network management interoperability by using ontology.pdf"
    )
    lista25 = busca(arquivo25)

    arquivo26 = pdfRead(
        "Semantic context dissemination and service matchmaking in future network management.pdf"
    )
    lista26 = busca(arquivo26)

    arquivo27 = pdfRead(
        "Semantic matching of security policies to support security experts.pdf"
    )
    lista27 = busca(arquivo27)

   # arquivo28 = pdfRead(
       # "Similarity and logic based ontology mapping for security management.pdf")
    #lista28 = busca(arquivo28)

    arquivo29 = pdfRead(
        "SINMS- A slow intelligence network manager based on SNMP protocol.pdf")
    lista29 = busca(arquivo29)

    arquivo30 = pdfRead(
        "The STAC (security toolbox- Attacks _ countermeasures) ontology.pdf")
    lista30 = busca(arquivo30)

    arquivo31 = pdfRead(
        "Towards an information model that supports service-aware, self-managing virtual resources.pdf"
    )
    lista31 = busca(arquivo31)

    arquivo32 = pdfRead(
        "Towards automation for pervasive network security management using an integration of ontology-based and policy-based approaches.pdf"
    )
    lista32 = busca(arquivo32)
    listaFinal = []
    i = 0
    
    while i < 16:
      
      listaFinal.append(lista1[i]+lista2[i]+lista3[i]+lista4[i]+lista5[i]+lista6[i]+lista7[i]+lista8[i]+lista9[i]+lista10[i]+lista11[i]+lista11[i]+lista12[i]+lista13[i]+lista14[i]+lista15[i]+lista16[i]+lista17[i]+lista18[i]+lista19[i]+lista20[i]+lista21[i]+lista22[i]+lista23[i]+lista24[i]+lista25[i]+lista26[i]+lista27[i]+lista29[i]+lista30[i]+lista31[i]+lista32[i])
      i += 1
    print(listaFinal)
    geraGrafico(listaFinal)
      


main()
