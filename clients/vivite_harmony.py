# -*- coding: utf-8 -*-
"""Vivite Harmony — configuração factual do cliente.

Site fora do ar em 21/10/2026 (Cloudflare 526): dados vindos do dossiê interno da Invictus.
Completar links, WhatsApp, endereço e CRM/CRO quando o site voltar.
"""
from core.models import ClientConfig, LinkInterno

CONFIG = ClientConfig(
    slug='vivite_harmony',
    nome='Vivite Harmony',
    especialidade='Clínica',
    segmento='saude',
    dominio_oficial='viviteharmony.com.br',

    cidade='Belo Horizonte',
    estado='MG',
    bairro='',  # FALTA: bairro não informado
    credenciais='',  # FALTA: CRM e CRO não confirmados
    servicos=[],  # FALTA: serviços específicos verificáveis no site, fora do ar
    publico='',  # FALTA: público não informado
    diferencial='medicina regenerativa',

    fatos_validados=[
        'Clínica em Belo Horizonte/MG',
        'Dossiê interno: dois pilares de atuação, ortopedia (Dr. Alexandre Martins, cirurgia de joelho e medicina da dor) e odontologia estética (harmonização facial)',
        'Medicina regenerativa como diferencial',
    ],
    restricoes=[
        'não prometer resultado',
        'Nunca prometer resultado: "médico que promete, mente"',
        'Não entrar em disputa médicos x dentistas',
        'Sem CRM/CRO confirmados, não declarar especialidades ou títulos profissionais, inclusive a partir dos pilares descritos no dossiê',
        'Não inventar endereço, WhatsApp, CRM, CRO ou páginas internas não verificadas',
    ],
    direcionamento='',  # FALTA: direcionamento editorial não informado

    links_internos=[
        LinkInterno('Home', 'https://viviteharmony.com.br/', 'Home'),
        LinkInterno('Blog', 'https://viviteharmony.com.br/blog/', 'Blog'),
    ],  # FALTA: demais páginas não verificáveis com o site fora do ar
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
    ],

    whatsapp='',  # FALTA: WhatsApp não informado
    enderecos=[],  # FALTA: endereço não informado
    assinatura='Vivite Harmony — Clínica em Belo Horizonte/MG',
)
