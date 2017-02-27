from fqhc_compliance_tool.models import Requirement, SubRequirement
import json

def add_dummy_data():
    for n in range(1,20):
        requirement = Requirement(
            step=n,
            name="Dummy requirement %s" % (n,),
            text="The default text for dummy requirement %s" % (n,))
        requirement.save()
        for m in range(1,4):
            subrequirement = SubRequirement(
                requirement=requirement,
                step=m,
                name="Dummy subrequirement %s" % (m,),
                text="The default text for dummy subrequirement %s" % (m,))
            subrequirement.save()
