# Placeholder for company_profile.py
company_info = {
    "name": "Arvitai Technology",
    "owner": "Krishna Gupta",
    "address": "Mansarovar, Rajasthan, India",
    "phone": "+91-70232641337",
    "email": "support@arviitai.com",
    "type": "Software Services & Custom Product Development Company",
    "services": [
        "Web App Development",
        "Mobile App Development",
        "AI/ML Solutions",
        "Cloud & DevOps",
        "ERP/CRM Systems",
        "SaaS Platforms",
        "API Integrations"
    ]
}

def get_formatted_info():
    services = ", ".join(company_info["services"])
    return (
        f"{company_info['name']} is a {company_info['type']} founded by {company_info['owner']}, "
        f"based in {company_info['address']}. We specialize in {services}. "
        f"You can reach us at {company_info['phone']} or email us at {company_info['email']}."
    )
