from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from openai import OpenAI
import string

PATH = ".\config"

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
                            "type": "text",
                            "text": "Récupère une liste de mots\nGarde uniquement les mots qui sont des skills, softskills, technologies utile pour un poste\n(Retourne uniquement la liste des mots en format json)\n"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "[\"technologies\",\"innovantes\",\"approche\",\"résolument\",\"collaborative\",\"sopra\",\"steria\",\"place\",\"’\",\"humain\",\"centre\",\"action\",\"’\",\"engage\",\"auprès\",\"clients\",\"tirer\",\"meilleur\",\"parti\",\"digital\",\"construire\",\"avenir\",\"positif\",\"2023\",\"groupe\",\"a\",\"réalisé\",\"chiffre\",\"’\",\"affaires\",\"58\",\"milliards\",\"’\",\"euros\",\"the\",\"world\",\"is\",\"how\",\"we\",\"shape\",\"it\",\"description\",\"poste\",\"futur\",\"environnement\",\"travail\",\"intégrée\",\"équipe\",\"sopra\",\"steria\",\"denviron\",\"10\",\"personnes\",\"formation\",\"daccueil\",\"personnalisée\",\"cycle\",\"conférences\",\"technologies\",\"produits\",\"usités\",\"sein\",\"projet\",\"délivrée\",\"cours\",\"stage\",\"rôle\",\"missions\",\"rattachée\",\"agence\",\"dynamique\",\"plein\",\"essor\",\"évoluez\",\"environnement\",\"challengeant\",\"convivial\",\"entourée\",\"passionnés\",\"dotés\",\"dexpertises\",\"leurs\",\"domaines\",\"missions\",\"développement\",\"recherche\",\"solutions\",\"problématiques\",\"techniques\",\"lindustrialisation\",\"lanimation\",\"participation\",\"daily\",\"meeting\",\"technologies\",\"utilisées\",\"java\",\"javascript\",\"nodejs\",\"vuejs\"]"
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "text": "{\n    \"softskills\": [\"collaborative\", \"humain\", \"engagement\", \"positif\", \"communication\", \"travail d'équipe\", \"adaptabilité\"],\n    \"technologies\": [\"java\", \"javascript\", \"nodejs\", \"vuejs\"]\n}",
                            "type": "text"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "[\"angular\",\"reactjs\",\"apports\",\"stage\",\"améliorer\",\"compétences\",\"nouvelles\",\"technologies\",\"comprendre\",\"cycle\",\"développement\",\"dune\",\"application\",\"appréhender\",\"enjeux\",\"objectifs\",\"projet\",\"afin\",\"dy\",\"apporter\",\"contribution\",\"être\",\"intégrée\",\"équipe\",\"expérimentée\",\"outils\",\"méthodes\",\"développement\",\"qualifications\",\"rigoureuxse\",\"méthodique\",\"possédez\",\"fort\",\"esprit\",\"’\",\"équipe\",\"’\",\"initiative\",\"étudiante\",\"école\",\"dingénieurs\",\"master\",\"informatique\",\"équivalent\",\"recherchez\",\"stage\",\"fin\",\"’\",\"études\",\"souhaitez\",\"investir\",\"projets\",\"forts\",\"enjeux\",\"sociétaux\",\"alliant\",\"challenge\",\"innovation\",\"alors\",\"intégrez\",\"entreprise\",\"où\",\"règne\",\"esprit\",\"entrepreneurial\",\"fort\",\"atmosphère\",\"propice\",\"évolution\",\"participez\",\"sans\",\"plus\",\"attendre\",\"transformation\",\"durable\",\"grâce\",\"véritable\",\"aventure\",\"humaine\",\"sein\",\"dun\",\"grand\",\"groupe\",\"international\",\"informations\",\"supplémentaires\",\"proposons\",\"accord\",\"télétravail\",\"télétravailler\",\"jusquà\",\"2\",\"jours\",\"semaine\",\"selon\",\"missions\",\"package\",\"avantages\",\"intéressants\",\"titres\"]"
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "text": "{\n    \"softskills\": [\"adaptabilité\", \"rigoureux(se)\", \"méthodique\", \"esprit d'équipe\", \"initiative\", \"esprit entrepreneurial\"],\n    \"technologies\": [\"angular\", \"reactjs\"]\n}",
                            "type": "text"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "[\"client\",\"rédiger\",\"la\",\"documentation\",\"technique\",\"·\",\"tests\",\"recette\",\"définir\",\"les\",\"stratégies\",\"dintégration\",\"dossiers\",\"de\",\"tests\",\"participer\",\"et\",\"mettre\",\"en\",\"place\",\"du\",\"plan\",\"dintégration\",\"·\",\"identifier\",\"et\",\"traiter\",\"les\",\"dysfonctionnements\",\"du\",\"logiciel\",\"mots\",\"clés\",\"java\",\"angular\",\"vuejs\",\"mysql\",\"html5\",\"css3\",\"webservices\",\"rest\",\"docker\",\"jenkins\",\"react\",\"js\",\"intégration\",\"jenkins\",\"here\",\"at\",\"atos\",\"diversity\",\"and\",\"inclusion\",\"are\",\"embedded\",\"in\",\"our\",\"dna\",\"read\",\"more\",\"about\",\"our\",\"commitment\",\"to\",\"a\",\"fair\",\"work\",\"environment\",\"for\",\"all\",\"atos\",\"is\",\"a\",\"recognized\",\"leader\",\"in\",\"its\",\"industry\",\"across\",\"environment\",\"social\",\"and\",\"governance\",\"esg\",\"criteria\",\"find\",\"out\",\"more\",\"on\",\"our\",\"csr\",\"commitment\",\"choose\",\"your\",\"future\",\"choose\",\"atos\",\"learn\",\"more\",\"about\"]"
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "text": "{\n    \"softskills\": [\"rédaction\", \"analyse\", \"stratégie\", \"gestion des dysfonctionnements\", \"collaboration\", \"communication\"],\n    \"technologies\": [\"java\", \"angular\", \"vuejs\", \"mysql\", \"html5\", \"css3\", \"webservices\", \"rest\", \"docker\", \"jenkins\", \"reactjs\"]\n}",
                            "type": "text"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "['développeur', 'full', 'stack', 'js', 'confirmé', 'hf', 'goweb', 'lille', '59', '37', '000', '€', '47', '000', '€', 'an', 'cdi', 'temps', 'plein', 'détails', 'lemploi', 'correspondance', 'entre', 'poste', 'profil', 'salaire', '37', '000', '€', '47', '000', '€', 'an', 'type', 'poste', 'cdi', 'temps', 'plein\n', 'temps', 'travail', 'repos', 'weekend', 'travail', 'journée', 'lundi', 'vendredi', 'nbsp', 'lieu', 'lille', '59', 'nbsp', 'avantages', 'extraits', 'description', 'complète', 'poste', 'prise', 'charge', 'transport', 'quotidien', 'rtt', 'nbsp', 'description', 'poste', 'goweb', 'esn', 'taille', 'humaine', '\n40', 'collaborateurs', 'adressant', 'projets', 'internationaux', '’', 'optimisation', 'systèmes', '’', 'informations', 'applications', 'sites', 'depuis', 'plus', '25', 'ans', 'dynamique', 'collective', 'goweb', '’', 'articule', 'autour', 'deplusieurs', 'métiers', 'ux', 'ui', 'designers', 'développeurs', 'fr\nontend', 'développeurs', 'full', 'stack', 'js', 'développeurs', 'backend', 'product', 'managers', 'chefs', 'projet', 'technique', 'testeurs', 'quality', 'analyst', 'devops', 'chez', 'goweb', 'créons', 'lien', 'entre', 'métiers', 'amenons', 'sens', 'travail', 'aujourd', '’', 'hui', 'souhaitons', 'faire', 'gr\nandir', 'communauté', '’', 'experts', '’', 'pourquoi', 'recherchons', 'développeur', 'full', 'stack', 'confirmé', 'hf', 'prendre', 'part', 'projets', 'structurants', 'internationaux', 'quotidien', 'rôle', 'configurer', 'linfrastructure', 'matérielle', 'système', 'dexploitation', 'ainsi', 'dépendances', 'ent\nre', 'différents', 'composants', 'logiciels', 'utiliser', 'concevoir', 'manipuler', 'interroger', 'bases', 'données', 'concevoir', 'code', 'backend', 'api', 'daccès', 'données', 'sous', 'forme', 'webservices', 'utilisant', 'langages', 'tels', 'java', 'etou', 'nodejs', 'concevoir', 'code', 'frontend', 'exécu\nté', 'plateforme', 'lutilisateur', 'plus', 'souvent', 'smartphone', 'navigateur', 'web', 'langages', 'tels', 'javascript', 'frameworks', 'vuereact', 'être', 'capable', 'gérer', 'planifier', 'projet', 'méthodes', 'développement', 'agiles', 'telles', 'scrum', 'kanban', 'pouvoir', 'interagir', 'client', 'besoi\nns', 'documenter', 'lensemble', 'parties', 'projet', 'si', 'affinité', 'plus', 'étendue', '’', 'deux', 'couches', 'front', 'back', 'dois', 'être', 'familiarisé', 'chacune', 'dentre', 'elles', 'maîtrises', 'sujets', 'suivants', 'accessibilité', 'webperf', 'devops', 'cicd', 'conception', '’', 'architecture', \n'algorithmie', 'bon', 'niveau', 'danglais', 'technique', 'oral', 'écrit', 'compétences', 'techniques', 'côté', 'front', 'html', 'scss', 'sass', 'full', 'javascript', 'frameworks', 'vue', 'react', 'côté', 'back', 'java', 'jee', 'node', 'js', 'spring', 'boot', 'api', 'restful', 'postgre', 'mongodb', 'redis', \n'kafka', 'google', 'cloud', 'platform', 'aws', 'git', 'github', 'giblab', 'cicd', 'docker', 'kubernetes', 'jira', 'cleancode', 'test', 'driven', 'development', 'quotidien', 'personne', 'engagée', 'investie', 'proactif', 'travail', 'capacité', 'fournir', 'solutions', 'sortent', 'parfois', 'cadre', 'bonne', '\ncapacité', 'relationnelle', 'mode', 'openness', 'échanges', 'coconstruis', 'interdépendance', 'forte', '’', 'it', 'métiers', 'mode', 'solution', 'service', 'client', 'amener', 'qualité', 'rapidité', 'mises', 'production', 'expérience', 'également', 'capacité', '’', 'animer', 'ateliers', 'techniques', 'réali\nser', 'feedback', 'prendre', 'lead', 'certains', 'sujets', 'retrouves', 'cette', 'annonce', '’', 'hésite', 'postule', 'échangerons', 'parcours', 'recherches', 'aujourd', '’', 'hui', '’', 'point', 'vue', 'professionnel', 'type', 'demploi', 'temps', 'plein', 'cdi', 'statut', 'cadre', 'rémunération', '37', '00\n000€', '47', '00000€', 'an', 'avantages', 'prise', 'charge', 'transport', 'quotidien', 'rtt', 'horaires', 'lundi', 'vendredi', 'repos', 'weekend', 'travail', 'journée', 'rémunération', 'supplémentaire', 'primes', 'expérience', 'développement', 'web', '5', 'ans', 'requis', 'lieu', 'poste', 'présentiel', 'nbsp', 'nbsp', 'signaler', 'loffre', 'informations', 'transparence', 'lannonce']"
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": "{\n    \"softskills\": [\"proactivité\", \"résolution de problèmes\", \"capacité relationnelle\", \"communication\", \"travail en équipe\", \"adaptabilité\", \"leadership\"],\n    \"technologies\": [\"html\", \"scss\", \"sass\", \"javascript\", \"vue\", \"react\", \"java\", \"jee\", \"nodejs\", \"spring boot\", \"restful api\", \"postgre\", \"mongodb\", \"redis\", \"kafka\", \"google cloud platform\", \"aws\", \"git\", \"docker\", \"kubernetes\", \"jira\", \"cleancode\", \"test driven development\"]\n}"
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
                }
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
