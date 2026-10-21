# -*- coding: utf-8 -*-
"""Dra. Diana Mendes — configuração factual do cliente."""
from core.models import ClientConfig, LinkInterno

CONFIG = ClientConfig(
    slug='dra_diana',
    nome='Dra. Diana Mendes',
    especialidade='Dermatologia Clínica e Estética',
    segmento='saude',
    dominio_oficial='dradianamendes.com.br',

    cidade='Imperatriz',
    estado='MA',
    bairro='Centro',
    credenciais='CRM-MA 9398 | RQE 2912',
    servicos=[
        'rejuvenescimento facial (toxina)',
        'Liftera ultrassom microfocado',
        'Sculptra e bioestimuladores',
        'preenchedores (ácido hialurônico)',
        'manchas e cicatrizes',
        'prick test e patch test',
        'pequenas cirurgias e biópsia',
    ],
    publico='',  # FALTA: público não informado
    diferencial='diagnóstico antes de qualquer procedimento; beleza com naturalidade e segurança',

    fatos_validados=[
        'Dermatologista com residência médica',
        'Atendimento na Clínica DermCare, em Imperatriz/MA',
        'Diagnóstico antes de qualquer procedimento; beleza com naturalidade e segurança',
    ],
    restricoes=[
        'não prometer resultado',
    ],
    direcionamento='',  # FALTA: direcionamento editorial não informado

    links_internos=[
        LinkInterno('Home', 'https://dradianamendes.com.br/', 'Home'),
        LinkInterno('Sobre', 'https://dradianamendes.com.br/sobre/', 'Sobre'),
        LinkInterno('Procedimentos', 'https://dradianamendes.com.br/procedimentos/', 'Procedimentos'),
        LinkInterno('A Clínica', 'https://dradianamendes.com.br/a-clinica/', 'A Clínica'),
        LinkInterno('Blog', 'https://dradianamendes.com.br/blog/', 'Blog'),
        LinkInterno('Contato', 'https://dradianamendes.com.br/contato/', 'Contato'),
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
        'sbd.org.br',
    ],

    whatsapp='https://wa.me/559991295979',
    enderecos=[
        'Rua Urbano Santos, 155, Sala 1711, 17º andar – Centro (em frente ao Centro de Convenções) – Imperatriz/MA',
    ],
    assinatura='Dra. Diana Mendes — Dermatologia Clínica e Estética em Imperatriz/MA | CRM-MA 9398 | RQE 2912',
)
