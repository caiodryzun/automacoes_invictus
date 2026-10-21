# -*- coding: utf-8 -*-
"""Dra. Luani Peter — configuração factual do cliente."""
from core.models import ClientConfig, LinkInterno

CONFIG = ClientConfig(
    slug='dra_luani',
    nome='Dra. Luani Peter',
    especialidade='Estética Avançada (Biomedicina Estética)',
    segmento='saude',
    dominio_oficial='draluanipeter.com.br',

    cidade='Tapejara',
    estado='RS',
    bairro='',  # FALTA: bairro não informado
    credenciais='',  # FALTA: CRBM não encontrado
    servicos=[
        'gerenciamento de pele (limpeza, peelings)',
        'refinamento facial',
        'refinamento corporal (volumização glútea)',
        'mentoria e cursos para profissionais',
    ],
    publico='',  # FALTA: público não informado
    diferencial='estética individualizada, segura e baseada em ciência; menos excessos, mais naturalidade',

    fatos_validados=[
        'Luani Peter é biomédica esteta e diretora técnica, não médica',
        'Clínica de estética em Tapejara/RS, desde 2013',
        'Estética individualizada, segura e baseada em ciência; menos excessos, mais naturalidade',
    ],
    restricoes=[
        'não prometer resultado',
        'Luani Peter é biomédica esteta e não médica: nunca chamar de médica nem atribuir CRM',
        'Não inventar registro CRBM: não encontrado',
        'Usar a grafia Luani Peter',
    ],
    direcionamento='',  # FALTA: direcionamento editorial não informado

    links_internos=[
        LinkInterno('Home', 'https://draluanipeter.com.br/', 'Home'),
        LinkInterno('Sobre', 'https://draluanipeter.com.br/sobre/', 'Sobre'),
        LinkInterno('Procedimentos', 'https://draluanipeter.com.br/procedimentos/', 'Procedimentos'),
        LinkInterno('Blog', 'https://draluanipeter.com.br/blog/', 'Blog'),
        LinkInterno('Contato', 'https://draluanipeter.com.br/contato/', 'Contato'),
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
        'crbm.org.br',
        'cfbm.gov.br',
    ],

    whatsapp='https://wa.me/5554996791252',
    enderecos=[
        'Rua Ângelo Dalzotto, 822 – Tapejara/RS',
    ],
    assinatura='Dra. Luani Peter — Estética Avançada (Biomedicina Estética) em Tapejara/RS',
)
