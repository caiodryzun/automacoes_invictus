# -*- coding: utf-8 -*-
"""Dr. Wiler Costa — configuração factual do cliente."""
from core.models import ClientConfig, LinkInterno

CONFIG = ClientConfig(
    slug='dr_wiler',
    nome='Dr. Wiler Costa',
    especialidade='Ginecologia e Obstetrícia (menopausa, climatério e reposição hormonal)',
    segmento='saude',
    dominio_oficial='drwilercosta.com.br',

    cidade='São Paulo',
    estado='SP',
    bairro='Brooklin',
    credenciais='CRM-SP 195343 | RQE 76874',
    servicos=[
        'Ginecologia e Obstetrícia',
        'menopausa, climatério e reposição hormonal',
        'consultas presenciais (Brooklin) ou teleconsulta',
    ],
    publico='',  # FALTA: público não informado
    diferencial='consulta de 1 hora; atendimento particular com nota para reembolso',

    fatos_validados=[
        'Pós-graduação em Nutrologia no Instituto Israelita Albert Einstein',
        'Consultas presenciais no Brooklin ou teleconsulta',
        'Consulta de 1 hora; atendimento particular com nota para reembolso',
    ],
    restricoes=[
        'não prometer resultado',
        'Não apresentar pós-graduação em Nutrologia como título de especialista em Nutrologia',
    ],
    direcionamento='',  # FALTA: direcionamento editorial não informado

    links_internos=[
        LinkInterno('Home', 'https://drwilercosta.com.br/', 'Home'),
        LinkInterno('Dr. Wiler Costa', 'https://drwilercosta.com.br/dr-wiler-costa/', 'Dr. Wiler Costa'),
        LinkInterno('Especialidades', 'https://drwilercosta.com.br/especialidades/', 'Especialidades'),
        LinkInterno('Implante Hormonal', 'https://drwilercosta.com.br/especialidades/implante-hormonal/', 'Implante Hormonal'),
        LinkInterno('Cirurgia Íntima', 'https://drwilercosta.com.br/especialidades/cirurgia-intima/', 'Cirurgia Íntima'),
        LinkInterno('Emagrecimento e Performance', 'https://drwilercosta.com.br/especialidades/emagrecimento-e-performance/', 'Emagrecimento e Performance'),
        LinkInterno('Consultório', 'https://drwilercosta.com.br/consultorio/', 'Consultório'),
        LinkInterno('Atendimento', 'https://drwilercosta.com.br/atendimento/', 'Atendimento'),
        LinkInterno('Blog', 'https://drwilercosta.com.br/blog/', 'Blog'),
        LinkInterno('Contato', 'https://drwilercosta.com.br/contato/', 'Contato'),
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
        'febrasgo.org.br',
        'sobrac.org.br',
        'menopause.org',
    ],

    whatsapp='https://wa.me/5511999479508',
    enderecos=[
        'R. Barão do Triunfo, 612 — Conj. 2205 – Brooklin – São Paulo/SP',
        'R. Barão do Triunfo, 88 — 11º andar · Conj. 1101 – São Paulo/SP',
        'Alameda dos Aicás, 258 — Clínica Oppermann – São Paulo/SP',
    ],
    assinatura='Dr. Wiler Costa — Ginecologia e Obstetrícia (menopausa, climatério e reposição hormonal) em São Paulo/SP | CRM-SP 195343 | RQE 76874',
)
