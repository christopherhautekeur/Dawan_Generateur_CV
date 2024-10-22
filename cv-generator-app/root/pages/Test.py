from root.utils.PageCreator import PageCreator

page = PageCreator(
    "Dawan Générateur de CV - Test tuto",
    "Tuto",
    "Tuto",
    "",
)

tutorial_steps = {
    "Motivation Header": [
        "Bienvenue à la première étape ! Ici, nous allons commencer par écrire une lettre de motivation efficace.",
        "Commencez par une salutation appropriée, comme 'Madame, Monsieur' si vous ne connaissez pas le nom du recruteur.",
        "Dans le premier paragraphe, présentez-vous et expliquez pourquoi vous postulez à cette offre.",
        "Décrivez ensuite vos compétences et expériences pertinentes, en soulignant ce que vous pouvez apporter à l'entreprise.",
        "Terminez par une conclusion positive et professionnelle, en indiquant que vous êtes disponible pour un entretien."
    ],
    "CV Header": [
        "Passons à la rédaction de votre CV ! Un CV bien structuré est essentiel pour attirer l'attention des recruteurs.",
        "Commencez par vos informations personnelles : nom, adresse, email, numéro de téléphone.",
        "Ensuite, décrivez votre objectif professionnel en quelques lignes, en mentionnant le poste que vous visez.",
        "Listez vos expériences professionnelles les plus récentes, en commençant par la plus récente, et détaillez vos tâches principales.",
        "Ajoutez vos compétences clés, comme les langues parlées, les compétences informatiques, ou autres compétences techniques.",
        "Terminez par la section formation, en listant vos diplômes du plus récent au plus ancien."
    ],
    "Alternance Header": [
        "Pour une candidature en alternance, il est important de bien préciser votre parcours académique et vos objectifs professionnels.",
        "Expliquez dans un paragraphe pourquoi vous recherchez une alternance et ce que vous attendez de cette expérience.",
        "Soulignez les compétences que vous souhaitez développer et comment cette alternance peut vous aider dans votre carrière.",
        "Ajoutez des informations sur vos disponibilités, le rythme d'alternance souhaité (par exemple, 3 jours en entreprise, 2 jours à l'école).",
        "N'oubliez pas de mentionner vos expériences ou projets académiques liés au poste pour lequel vous postulez."
    ]
}

page.create_tutorial(tutorial_steps)
