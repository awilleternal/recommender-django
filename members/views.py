
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from members import recommender




def members(request):
    if request.method == 'POST':
        result = request.POST
        requirement = {
            "REQUIREMENT": {
                "HTML": int(result['html']),
                "Python": int(result['python']),
                "Java": int(result['java']),
                "C": int(result['c']),
                "JavaScript": int(result['javascript'])
            }
        }
        num_of_candidate = int(result['candidate'])
        result = recommender.topMatches(requirement, recommender.dataFrame, "REQUIREMENT", num_of_candidate)
        print(result)
        return render(request, "index.html", {'result': result})

    return render(request, "index.html", {'result': [("name", "Score")]})
    # try:
    #     if request.method == 'POST':
    #         result = request.POST
    #         result=loader.get_template('index.html')
    #         requirement = {"REQUIREMENT": {
    #             "HTML": int(result['html']),
    #             "Python": int(result['python']),
    #             "Java": int(result['java']),
    #             "C": int(result['c']),
    #             "JavaScript": int(result['javascript'])}}
    #         num_of_candidate = int(result['candidate'])
        
        
    #         result = recommender.topMatches(requirement, recommender.dataFrame, "REQUIREMENT", num_of_candidate)
    #         print(result)
    #         return ("index.html",result=result)
    # except:
    #     pass
    
    # return HttpResponse(result.render(),result[("name","Score")])

# Create your views here.
# def hello_world():
#     if request.method == 'POST':
#         result = request.form
#         requirement = {"REQUIREMENT": {
#             "HTML": int(result['html']),
#             "Python": int(result['python']),
#             "Java": int(result['java']),
#             "C": int(result['c']),
#             "JavaScript": int(result['javascript'])}}
#         num_of_candidate = int(result['candidate'])
#         result = recommender.topMatches(requirement, recommender.dataFrame, "REQUIREMENT", num_of_candidate)
#         print(result)
#         return ("index.html", result=result)

#     return render_template("index.html", result=[("name","Score")])
