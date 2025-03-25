# hash_folder
Este script Python calcula hashes SHA-256 para todos os arquivos em um diretório especificado e salva os resultados em um arquivo CSV. A verificação de hashes é uma prática fundamental na segurança da informação para garantir a integridade de dados.

Importância para Segurança da Informação

    Verificação de Integridade: Hashes permitem detectar alterações em arquivos, sejam acidentais ou maliciosas

    Detecção de Manipulação: Qualquer modificação em um arquivo alterará completamente seu valor de hash

    Proteção de Dados Sensíveis: Embora não processe conteúdos diretamente, a geração de hash é etapa crítica em fluxos de proteção de dados

    Rastreamento de Auditoria: O CSV gerado serve como registro verificável do estado dos arquivos em um momento específico
    Funcionalidades

    Processa recursivamente todos os arquivos em um diretório

    Ignora arquivos ocultos (iniciados com .) e arquivos de sistema como desktop.ini

    Processa arquivos grandes de forma eficiente com leitura em blocos

    Registro detalhado de erros (logging)

    Gera relatório em CSV com pares nome_arquivo/hash
    
    Como Usar:
    Saída

O script gera um arquivo CSV com duas colunas:

    Nome do Arquivo: Nome do arquivo

    Hash SHA-256: Hash SHA-256 correspondente

Considerações de Segurança

    Proteja o CSV gerado: O arquivo de hashes deve ser armazenado com segurança, pois pode ser usado para verificar conteúdos

    Combine com criptografia: Para máxima segurança, use junto com armazenamento criptografado para dados sensíveis

    Verificação periódica: Execute regularmente para detectar alterações não autorizadas

    Controles de acesso: Garanta que apenas pessoal autorizado tenha acesso aos arquivos originais e relatórios de hash
