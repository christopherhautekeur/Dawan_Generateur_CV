from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from openai import OpenAI
import string

PATH = ".\cv-generator-app\config"

class Processing:
    def __init__(self):
        file = open(PATH, 'r')
        lines = file.readlines()
        self.client = OpenAI(
            api_key=lines[0].split('=')[1].strip()
        )
        self.stop_words = set(stopwords.words('french'))

    def process_jobs_infos(self, infos):
        """
        Filter tokens from infos to get softskills and skills
        :param infos: tokens from jobs offer descriptions
        :return:  a String of softskills and skills in json format
        """
        infos = self.tokenize(infos)

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "text": "Récupère une liste de mots\nGarde uniquement les mots qui sont des skills, "
                                    "softskills, technologies utile pour un poste\nRetourne un json\n",
                            "type": "text"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "[\"technologies\",\"innovantes\",\"approche\",\"résolument\",\"collaborative\","
                                    "\"sopra\",\"steria\",\"place\",\"’\",\"humain\",\"centre\",\"action\",\"’\","
                                    "\"engage\",\"auprès\",\"clients\",\"tirer\",\"meilleur\",\"parti\",\"digital\","
                                    "\"construire\",\"avenir\",\"positif\",\"2023\",\"groupe\",\"a\",\"réalisé\","
                                    "\"chiffre\",\"’\",\"affaires\",\"58\",\"milliards\",\"’\",\"euros\",\"the\","
                                    "\"world\",\"is\",\"how\",\"we\",\"shape\",\"it\",\"description\",\"poste\","
                                    "\"futur\",\"environnement\",\"travail\",\"intégrée\",\"équipe\",\"sopra\","
                                    "\"steria\",\"denviron\",\"10\",\"personnes\",\"formation\",\"daccueil\","
                                    "\"personnalisée\",\"cycle\",\"conférences\",\"technologies\",\"produits\","
                                    "\"usités\",\"sein\",\"projet\",\"délivrée\",\"cours\",\"stage\",\"rôle\","
                                    "\"missions\",\"rattachée\",\"agence\",\"dynamique\",\"plein\",\"essor\","
                                    "\"évoluez\",\"environnement\",\"challengeant\",\"convivial\",\"entourée\","
                                    "\"passionnés\",\"dotés\",\"dexpertises\",\"leurs\",\"domaines\",\"missions\","
                                    "\"développement\",\"recherche\",\"solutions\",\"problématiques\",\"techniques\","
                                    "\"lindustrialisation\",\"lanimation\",\"participation\",\"daily\",\"meeting\","
                                    "\"technologies\",\"utilisées\",\"java\",\"javascript\",\"nodejs\",\"vuejs\"]"
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "text": "{\n    \"softskills\": [\"collaborative\", \"humain\", \"engagement\", "
                                    "\"positif\", \"communication\", \"travail d'équipe\", \"adaptabilité\"],"
                                    "\n    \"technologies\": [\"java\", \"javascript\", \"nodejs\", \"vuejs\"]\n}",
                            "type": "text"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "[\"angular\",\"reactjs\",\"apports\",\"stage\",\"améliorer\",\"compétences\","
                                    "\"nouvelles\",\"technologies\",\"comprendre\",\"cycle\",\"développement\","
                                    "\"dune\",\"application\",\"appréhender\",\"enjeux\",\"objectifs\",\"projet\","
                                    "\"afin\",\"dy\",\"apporter\",\"contribution\",\"être\",\"intégrée\",\"équipe\","
                                    "\"expérimentée\",\"outils\",\"méthodes\",\"développement\",\"qualifications\","
                                    "\"rigoureuxse\",\"méthodique\",\"possédez\",\"fort\",\"esprit\",\"’\","
                                    "\"équipe\",\"’\",\"initiative\",\"étudiante\",\"école\",\"dingénieurs\","
                                    "\"master\",\"informatique\",\"équivalent\",\"recherchez\",\"stage\",\"fin\","
                                    "\"’\",\"études\",\"souhaitez\",\"investir\",\"projets\",\"forts\",\"enjeux\","
                                    "\"sociétaux\",\"alliant\",\"challenge\",\"innovation\",\"alors\",\"intégrez\","
                                    "\"entreprise\",\"où\",\"règne\",\"esprit\",\"entrepreneurial\",\"fort\","
                                    "\"atmosphère\",\"propice\",\"évolution\",\"participez\",\"sans\",\"plus\","
                                    "\"attendre\",\"transformation\",\"durable\",\"grâce\",\"véritable\","
                                    "\"aventure\",\"humaine\",\"sein\",\"dun\",\"grand\",\"groupe\","
                                    "\"international\",\"informations\",\"supplémentaires\",\"proposons\",\"accord\","
                                    "\"télétravail\",\"télétravailler\",\"jusquà\",\"2\",\"jours\",\"semaine\","
                                    "\"selon\",\"missions\",\"package\",\"avantages\",\"intéressants\",\"titres\"]"
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "text": "{\n    \"softskills\": [\"adaptabilité\", \"rigoureux(se)\", \"méthodique\", "
                                    "\"esprit d'équipe\", \"initiative\", \"esprit entrepreneurial\"],"
                                    "\n    \"technologies\": [\"angular\", \"reactjs\"]\n}",
                            "type": "text"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "[\"client\",\"rédiger\",\"la\",\"documentation\",\"technique\",\"·\",\"tests\","
                                    "\"recette\",\"définir\",\"les\",\"stratégies\",\"dintégration\",\"dossiers\","
                                    "\"de\",\"tests\",\"participer\",\"et\",\"mettre\",\"en\",\"place\",\"du\","
                                    "\"plan\",\"dintégration\",\"·\",\"identifier\",\"et\",\"traiter\",\"les\","
                                    "\"dysfonctionnements\",\"du\",\"logiciel\",\"mots\",\"clés\",\"java\","
                                    "\"angular\",\"vuejs\",\"mysql\",\"html5\",\"css3\",\"webservices\",\"rest\","
                                    "\"docker\",\"jenkins\",\"react\",\"js\",\"intégration\",\"jenkins\",\"here\","
                                    "\"at\",\"atos\",\"diversity\",\"and\",\"inclusion\",\"are\",\"embedded\",\"in\","
                                    "\"our\",\"dna\",\"read\",\"more\",\"about\",\"our\",\"commitment\",\"to\",\"a\","
                                    "\"fair\",\"work\",\"environment\",\"for\",\"all\",\"atos\",\"is\",\"a\","
                                    "\"recognized\",\"leader\",\"in\",\"its\",\"industry\",\"across\","
                                    "\"environment\",\"social\",\"and\",\"governance\",\"esg\",\"criteria\",\"find\","
                                    "\"out\",\"more\",\"on\",\"our\",\"csr\",\"commitment\",\"choose\",\"your\","
                                    "\"future\",\"choose\",\"atos\",\"learn\",\"more\",\"about\"]"
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "text": "{\n    \"softskills\": [\"rédaction\", \"analyse\", \"stratégie\", \"gestion des "
                                    "dysfonctionnements\", \"collaboration\", \"communication\"],"
                                    "\n    \"technologies\": [\"java\", \"angular\", \"vuejs\", \"mysql\", \"html5\", "
                                    "\"css3\", \"webservices\", \"rest\", \"docker\", \"jenkins\", \"reactjs\"]\n}",
                            "type": "text"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": ''.join(infos),
                        }
                    ]
                },
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={
                "type": "text"
            }
        )
        return response.choices[0].message.content

    def tokenize(self, infos):
        """
        Tokenize jobs infos
        :param infos: offer's descriptions
        :return: array of tokens
        """
        tokens = []
        for info in infos:
            info = info.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
            tokens.append(word_tokenize(info.lower()))
        tokens = [token for token in tokens[0] if token not in self.stop_words]  # Remove stopwords

        return tokens
