# -*- coding: utf-8 -*-
"""Pousada Mazé — hospitalidade familiar à beira-mar (Itanhaém/SP).

Cliente no modelo config-driven: apenas DADOS. O pipeline é compartilhado
(ver pipeline/builder.py). Segmento comercial (não regulado) → tom persuasivo.
"""
from core.models import ClientConfig, LinkInterno

CONFIG = ClientConfig(
    slug="pousada_maze",
    nome="Pousada Mazé",
    especialidade="hospitalidade familiar à beira-mar",
    segmento="comercial",
    dominio_oficial="pousadamaze.com.br",

    cidade="Itanhaém",
    estado="SP",
    bairro="Cibratel",
    # Apenas atributos REAIS e concretos (sem termos abstratos como "lazer
    # refrescante" / "segurança total"). servicos_resumo usa os 4 primeiros.
    servicos=[
        "café da manhã incluso",
        "piscina",
        "estacionamento gratuito",
        "Wi-Fi gratuito",
        "quartos para casais e famílias",
        "acesso às praias do Cibratel e Cibratel 2 (pé na areia)",
        "atendimento acolhedor",
    ],
    publico=(
        "famílias e casais que buscam conforto, simplicidade e momentos "
        "inesquecíveis perto do mar"
    ),
    diferencial=(
        "hospitalidade familiar à beira-mar em Itanhaém, no bairro de Cibratel, "
        "a poucos passos da Praia do Cibratel e da Praia do Cibratel 2, desde 2025"
    ),

    # ── Guardrails factuais (feedback da revisão de conteúdo) ──────────────────
    fatos_validados=[
        "Localização no bairro de Cibratel, em Itanhaém/SP",
        "A poucos passos da Praia do Cibratel e da Praia do Cibratel 2 (acesso pé na areia)",
        "Piscina",
        "Café da manhã incluso",
        "Estacionamento gratuito",
        "Wi-Fi",
        "Quartos para casais e famílias",
        "Atendimento acolhedor / hospitalidade familiar (em operação desde 2025)",
        "Ar-condicionado disponível em APENAS UM quarto — quando o tema exigir, citar "
        "exatamente como: \"consulte a disponibilidade de acomodação com ar-condicionado "
        "pelo WhatsApp\" (nunca como comodidade padrão da pousada)",
    ],
    restricoes=[
        "piscina rasa",
        "parquinho",
        "copa baby",
        "berços",
        "cadeirões",
        "alimentação/cardápio infantil",
        "ar-condicionado como comodidade padrão (existe em apenas um quarto)",
    ],
    direcionamento=(
        "Mesmo quando o artigo tratar de temas gerais (turismo, praias, viagem, "
        "Itanhaém/Cibratel), conduza naturalmente o leitor a considerar a Pousada Mazé "
        "como opção de hospedagem em Itanhaém, sem inventar atributos."
    ),

    links_internos=[
        LinkInterno("Home — Pousada Mazé", "https://pousadamaze.com.br/",
                    "página inicial da pousada"),
        LinkInterno("Sobre Nós", "https://pousadamaze.com.br/sobre-nos/",
                    "conheça nossa história e refúgio"),
        LinkInterno("Blog", "https://pousadamaze.com.br/blog/",
                    "guia de descanso no litoral"),
    ],
    whitelist_externos=[
        ".gov", ".gov.br",
        "itanhaem.sp.gov.br", "turismosp.com.br", "gov.br",
        "developers.google.com", "schema.org", "w3.org",
        "moz.com", "ahrefs.com", "semrush.com",
    ],

    whatsapp="https://wa.link/xwl8kg",
    enderecos=[
        "R. Profa. Dalva Dati Ruivo, 70 – Cibratel – Itanhaém/SP – CEP 11746-274",
    ],
    assinatura="Pousada Mazé — Hospitalidade familiar à beira-mar em Itanhaém/SP",
    assinatura_intro=(
        "Para conhecer a pousada, tirar dúvidas ou garantir sua reserva, "
        "a nossa equipe está à disposição."
    ),
    cta_whatsapp_label="Reserve sua estadia pelo WhatsApp",
    # target_palavras / teto_palavras herdados do default (700-850, teto 900)
)
