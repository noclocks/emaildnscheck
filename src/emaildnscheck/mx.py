import dns.resolver

domain = "noclocks.dev"

answers = dns.resolver.resolve(domain, 'MX')
for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)
