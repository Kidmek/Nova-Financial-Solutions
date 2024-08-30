def analyze_publisher_contributions(data):
    # Count the number of articles per publisher
    publisher_counts = data['publisher'].value_counts().reset_index()
    publisher_counts.columns = ['Publisher', 'Article Count']

    # Sort by the number of articles contributed
    publisher_counts = publisher_counts.sort_values(by='Article Count', ascending=False)

    return publisher_counts

def analyze_publisher_domains(data):
    # Extract domain from email addresses if they are used as publisher names
    data['Domain'] = data['publisher'].apply(lambda x: x.split('@')[-1] if '@' in x else None)

    # Count the frequency of each domain
    domain_counts = data['Domain'].value_counts().reset_index()
    domain_counts.columns = ['Domain', 'Article Count']

    # Sort by the number of articles contributed by each domain
    domain_counts = domain_counts.sort_values(by='Article Count', ascending=False)

    return domain_counts