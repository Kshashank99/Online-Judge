# from rest_framework.response import Response
# from .models import solution,Question,testcase
# from .serializers import OjSerializer


# def getQuesionList(request):
#     question = Question.objects.all()
#     serializer = OjSerializer(question, many=True)
#     return Response(serializer.data)

# def getProblemDetail(request, pk):
#     question_details = Question.objects.get(id=pk)
#     serializer = OjSerializer(question_details, many=False)
#     return Response(serializer.data)  

# def ProblemSubmit(request,pk):
#     data = request.data
#     # submission_detail=  
#     # data = JSONParser().parse(request.data) 
#     try:
#         problem_body = solution.objects.get(id=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)        

#     # obj=get_object_or_404(Question, id = pk)
#     serializer = OjSerializer(problem_body, data=request.data)
#     if serializer.is_valid():
#             serializer.save()
#             # data["success"] = "update successful"
#             # sub = serializer.save()
#             # sub.curr_problem=obj
#             # sub.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)