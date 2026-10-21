# -*- coding: utf-8 -*-
"""Casa Vie Medicina (Dra. Larissa Barros) — configuração factual do cliente."""
from core.models import ClientConfig, LinkInterno

CONFIG = ClientConfig(
    slug='casa_vie',
    nome='Casa Vie Medicina (Dra. Larissa Barros)',
    especialidade='Dermatologia Integrativa, Tricologia, Estética Médica e Nutrologia',
    segmento='saude',
    dominio_oficial='casaviemedicina.com.br',

    cidade='São Paulo',
    estado='SP',
    bairro='Tatuapé',
    credenciais='',  # FALTA: CRM/RQE não encontrados no site
    servicos=[
        'Dermatologia Integrativa',
        'Tricologia',
        'Estética Médica',
        'Nutrologia',
        'Cardiologia',
    ],
    publico='',  # FALTA: público não informado
    diferencial='',  # FALTA: diferencial não informado

    fatos_validados=[
        'Casa Vie Medicina (Dra. Larissa Barros), no Tatuapé, São Paulo/SP',
        'Atuação em Dermatologia Integrativa, Tricologia, Estética Médica e Nutrologia; site também possui página de cardiologia',
    ],
    restricoes=[
        'não prometer resultado',
        'Não inventar CRM ou RQE; credenciais não encontradas no site',
    ],
    direcionamento='',  # FALTA: direcionamento editorial não informado

    links_internos=[
        LinkInterno('Home', 'https://www.casaviemedicina.com.br/', 'Home'),
        LinkInterno('Sobre', 'https://www.casaviemedicina.com.br/sobre/', 'Sobre'),
        LinkInterno('Especialidades', 'https://www.casaviemedicina.com.br/especialidades/', 'Especialidades'),
        LinkInterno('Dermatologia Integrativa', 'https://www.casaviemedicina.com.br/dermatologia-integrativa/', 'Dermatologia Integrativa'),
        LinkInterno('Tricologia e Saúde Capilar', 'https://www.casaviemedicina.com.br/tricologia-saude-capilar/', 'Tricologia e Saúde Capilar'),
        LinkInterno('Estética Médica', 'https://www.casaviemedicina.com.br/estetica-medica/', 'Estética Médica'),
        LinkInterno('Nutrologia e Nutrição', 'https://www.casaviemedicina.com.br/nutrologia-nutricao/', 'Nutrologia e Nutrição'),
        LinkInterno('Cardiologia e Longevidade', 'https://www.casaviemedicina.com.br/cardiologia-e-longevidade/', 'Cardiologia e Longevidade'),
        LinkInterno('Blog', 'https://www.casaviemedicina.com.br/blog/', 'Blog'),
        LinkInterno('Contato', 'https://www.casaviemedicina.com.br/contato/', 'Contato'),
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

    whatsapp='https://api.whatsapp.com/send?phone=5511993577760',
    enderecos=[
        'Rua Bom Sucesso 220, cj 3004 – Tatuapé – São Paulo/SP',
    ],
    assinatura='Casa Vie Medicina (Dra. Larissa Barros) — Dermatologia Integrativa, Tricologia, Estética Médica e Nutrologia em São Paulo/SP',
)
