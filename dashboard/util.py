from .models import Organization
from user.models import User


def get_org_info(orgid):
    organization = Organization.objects.get(orgid=orgid)
    return {
        'name': organization.name,
        'orgid': orgid,
        'description': organization.description,
        'initial_text': organization.initial_text
    }


def get_orgs_information():
    result = []
    for organization in Organization.objects.all():
        result.append(get_org_info(organization.orgid))
    return result


def get_org_replies(orgid):
    result = {}
    all_replies = Organization.objects.get(orgid=orgid).reply_set.all()
    for reply in all_replies:
        if str(reply.phone) not in result:
            result[str(reply.phone)] = [reply.message]
        else:
            result[str(reply.phone)].append(reply.message)
    return result


def get_org_users(orgid):
    result = []
    organization = Organization.objects.get(orgid=orgid)
    for a in range(0, int(len(organization.admins) / 4)):
        result.append(User.objects.get(userid=organization.admins[(a * 4): (a * 4 + 4)]))
    return result


def get_org_groups(orgid):
    result = []
    organization = Organization.objects.get(orgid=orgid)
    print()
    for group in organization.groups_set.all():
        result.append({
            'organization': group.organization,
            'active_window': group.active_window,
            'name': group.name,
            'description': group.description
        })

    return result
