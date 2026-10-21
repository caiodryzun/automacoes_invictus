# -*- coding: utf-8 -*-
"""Dr. Eduardo Dolci — configuração factual do cliente."""
from core.models import ClientConfig, LinkInterno

CONFIG = ClientConfig(
    slug='dr_dolci',
    nome='Dr. Eduardo Dolci',
    especialidade='Otorrinolaringologia e Cirurgia Estética Facial (rinoplastia)',
    segmento='saude',
    dominio_oficial='eduardodolci.com.br',

    cidade='São Paulo',
    estado='SP',
    bairro='',  # FALTA: bairro não informado
    credenciais='CRM 120.642 | RQE 83.410',
    servicos=[
        'cirurgia do nariz',
        'rinoplastia estética e funcional',
    ],
    publico='',  # FALTA: público não informado
    diferencial='professor da Santa Casa de São Paulo; fellowships em Stanford, Oregon e Chicago',

    fatos_validados=[
        'Atuação exclusiva em cirurgia do nariz',
        'Professor da Santa Casa de São Paulo; fellowships em Stanford, Oregon e Chicago',
    ],
    restricoes=[
        'não prometer resultado',
        'Não acrescentar UF ao CRM ou RQE: UF não explícita no site',
        'Não atribuir atuação fora da cirurgia do nariz',
    ],
    direcionamento='',  # FALTA: direcionamento editorial não informado

    links_internos=[
        LinkInterno('Home', 'https://www.eduardodolci.com.br/', 'Home'),
        LinkInterno('Quem Sou', 'https://www.eduardodolci.com.br/quem-sou/', 'Quem Sou'),
        LinkInterno('Rinoplastia Estética e Funcional', 'https://www.eduardodolci.com.br/rinoplastia-estetica-e-funcional/', 'Rinoplastia Estética e Funcional'),
        LinkInterno('Dicas e Dúvidas sobre Rinoplastia', 'https://www.eduardodolci.com.br/dicas-e-duvidas-sobre-rinoplastia/', 'Dicas e Dúvidas sobre Rinoplastia'),
        LinkInterno('Cuidados Pré-operatórios', 'https://www.eduardodolci.com.br/cuidados-pre-operatorios/', 'Cuidados Pré-operatórios'),
        LinkInterno('Cuidados Pós-operatórios', 'https://www.eduardodolci.com.br/cuidados-pos-operatorios/', 'Cuidados Pós-operatórios'),
        LinkInterno('Na Mídia', 'https://www.eduardodolci.com.br/na-midia/', 'Na Mídia'),
        LinkInterno('Vídeos', 'https://www.eduardodolci.com.br/videos/', 'Vídeos'),
        LinkInterno('Blog', 'https://www.eduardodolci.com.br/blog/', 'Blog'),
        LinkInterno('Contato', 'https://www.eduardodolci.com.br/contato/', 'Contato'),
    ],
    whitelist_externos=[
        '.gov',
        '.gov.br',
        '.edu',
        '.edu.br',
        'cfm.org.br',
        'who.int',
        'nhs.uk',
        'cdc.gov',
        'nih.gov',
        'ncbi.nlm.nih.gov',
        'medlineplus.gov',
        'cochranelibrary.com',
        'anvisa.gov.br',
        'schema.org',
        'w3.org',
        'developers.google.com',
        'support.google.com',
        'pubmed.ncbi.nlm.nih.gov',
        'scielo.br',
        'aborlccf.org.br',
    ],

    whatsapp='https://wa.me/5511997617353',
    enderecos=[
        'R. Dr. Bacelar, 173 · 5º andar, conj. 53 – São Paulo/SP',
    ],
    assinatura='Dr. Eduardo Dolci — Otorrinolaringologia e Cirurgia Estética Facial (rinoplastia) em São Paulo/SP | CRM 120.642 | RQE 83.410',
)
