from ..core.models import Company, Job


def get_company_by_user(user):
    try:
        company = Company.objects.get(user=user)
        if company:
            return company
    except:
        return False


def get_company_jobs(company):
    try:
        return Job.objects.filter(company=company)
    except:
        return None
