# Verde Vivo ONG - Plataforma Ambiental Cost Analysis Estimate Report

## Service Overview

Verde Vivo ONG - Plataforma Ambiental is a fully managed, serverless service that allows you to This project uses multiple AWS services.. This service follows a pay-as-you-go pricing model, making it cost-effective for various workloads.

## Pricing Model

This cost analysis estimate is based on the following pricing model:
- **ON DEMAND** pricing (pay-as-you-go) unless otherwise specified
- Standard service configurations without reserved capacity or savings plans
- No caching or optimization techniques applied

## Assumptions

- Tráfego baixo inicial (500 visitantes/mês)
- Site otimizado e leve (500MB)
- API com baixo volume (2000 chamadas/mês)
- Dados ambientais simples (100MB)
- Região us-east-1
- Foco em sustentabilidade e baixo custo

## Limitations and Exclusions

- Custos de desenvolvimento
- Certificados SSL customizados
- Backup avançado
- Suporte técnico premium
- Monitoramento de terceiros

## Cost Breakdown

### Unit Pricing Details

| Service | Resource Type | Unit | Price | Free Tier |
|---------|--------------|------|-------|------------|
| Amazon S3 | Storage | GB/mês (primeiros 50TB) | $0.023 | Primeiros 12 meses: 5GB gratuitos |
| Amazon CloudFront | Data Transfer | GB (primeiros 10TB) | $0.085 | Primeiros 12 meses: 50GB transferência gratuita |
| AWS Lambda | Compute | GB-second | $0.0000166667 | 1M execuções gratuitas/mês permanente |
| AWS Lambda | Requests | 1,000,000 requests | $0.20 | 1M execuções gratuitas/mês permanente |
| Amazon DynamoDB | Reads | 1,000,000 RCU | $0.25 | 25GB armazenamento + 25 RCU/WCU gratuitos |
| Amazon DynamoDB | Writes | 1,000,000 WCU | $1.25 | 25GB armazenamento + 25 RCU/WCU gratuitos |
| Amazon DynamoDB | Storage | GB/mês | $0.25 | 25GB armazenamento + 25 RCU/WCU gratuitos |
| Amazon API Gateway | Requests | 1,000,000 requests | $3.50 | Primeiros 12 meses: 1M chamadas gratuitas |
| Amazon CloudWatch | Metrics | metric/mês | $0.30 | 10 métricas customizadas gratuitas |

### Cost Calculation

| Service | Usage | Calculation | Monthly Cost |
|---------|-------|-------------|-------------|
| Amazon S3 | Site estático otimizado (500MB) (Storage: 0.5 GB total (site leve)) | $0.023 × 0.5 GB = $0.01/mês | $0.01 |
| Amazon CloudFront | 500 visitantes/mês, 20GB transferência (Data Transfer: 20 GB/mês) | Dentro do free tier | $0.00 |
| AWS Lambda | 2000 execuções/mês, 128MB, 100ms duração (Compute: 64 GB-seconds/mês, Requests: 2,000 requests/mês) | Dentro do free tier permanente | $0.00 |
| Amazon DynamoDB | 100MB dados ambientais, baixo volume (Operations: 500 reads + 100 writes, Storage: 0.1 GB) | Dentro do free tier | $0.00 |
| Amazon API Gateway | 2000 chamadas API/mês (Requests: 2,000 requests/mês) | Dentro do free tier | $0.00 |
| Amazon CloudWatch | Monitoramento básico de impacto (Metrics: 5 métricas ambientais) | Dentro do free tier | $0.00 |
| **Total** | **All services** | **Sum of all calculations** | **$0.01/month** |

### Free Tier

Free tier information by service:
- **Amazon S3**: Primeiros 12 meses: 5GB gratuitos
- **Amazon CloudFront**: Primeiros 12 meses: 50GB transferência gratuita
- **AWS Lambda**: 1M execuções gratuitas/mês permanente
- **Amazon DynamoDB**: 25GB armazenamento + 25 RCU/WCU gratuitos
- **Amazon API Gateway**: Primeiros 12 meses: 1M chamadas gratuitas
- **Amazon CloudWatch**: 10 métricas customizadas gratuitas

## Cost Scaling with Usage

The following table illustrates how cost estimates scale with different usage levels:

| Service | Low Usage | Medium Usage | High Usage |
|---------|-----------|--------------|------------|
| Amazon S3 | $0/month | $0/month | $0/month |
| Amazon CloudFront | Varies | Varies | Varies |
| AWS Lambda | Varies | Varies | Varies |
| Amazon DynamoDB | Varies | Varies | Varies |
| Amazon API Gateway | Varies | Varies | Varies |
| Amazon CloudWatch | Varies | Varies | Varies |

### Key Cost Factors

- **Amazon S3**: Site estático otimizado (500MB)
- **Amazon CloudFront**: 500 visitantes/mês, 20GB transferência
- **AWS Lambda**: 2000 execuções/mês, 128MB, 100ms duração
- **Amazon DynamoDB**: 100MB dados ambientais, baixo volume
- **Amazon API Gateway**: 2000 chamadas API/mês
- **Amazon CloudWatch**: Monitoramento básico de impacto

## Projected Costs Over Time

The following projections show estimated monthly costs over a 12-month period based on different growth patterns:

Base monthly cost calculation:

| Service | Monthly Cost |
|---------|-------------|
| Amazon S3 | $0.01 |
| **Total Monthly Cost** | **$0** |

| Growth Pattern | Month 1 | Month 3 | Month 6 | Month 12 |
|---------------|---------|---------|---------|----------|
| Steady | $0/mo | $0/mo | $0/mo | $0/mo |
| Moderate | $0/mo | $0/mo | $0/mo | $0/mo |
| Rapid | $0/mo | $0/mo | $0/mo | $0/mo |

* Steady: No monthly growth (1.0x)
* Moderate: 5% monthly growth (1.05x)
* Rapid: 10% monthly growth (1.1x)

## Detailed Cost Analysis

### Pricing Model

ON DEMAND


### Exclusions

- Custos de desenvolvimento
- Certificados SSL customizados
- Backup avançado
- Suporte técnico premium
- Monitoramento de terceiros

### Recommendations

#### Immediate Actions

- Aproveitar AWS Free Tier para ONG sem custos iniciais
- Otimizar imagens para reduzir transferência
- Implementar cache agressivo no CloudFront
#### Best Practices

- Monitorar uso mensal para manter dentro do free tier
- Configurar alertas de billing
- Usar compressão gzip para reduzir transferência
- Implementar lazy loading para imagens



## Cost Optimization Recommendations

### Immediate Actions

- Aproveitar AWS Free Tier para ONG sem custos iniciais
- Otimizar imagens para reduzir transferência
- Implementar cache agressivo no CloudFront

### Best Practices

- Monitorar uso mensal para manter dentro do free tier
- Configurar alertas de billing
- Usar compressão gzip para reduzir transferência

## Conclusion

By following the recommendations in this report, you can optimize your Verde Vivo ONG - Plataforma Ambiental costs while maintaining performance and reliability. Regular monitoring and adjustment of your usage patterns will help ensure cost efficiency as your workload evolves.
