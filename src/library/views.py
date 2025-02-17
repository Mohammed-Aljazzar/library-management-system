from django.shortcuts import render, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def book_list(request):
    # استرداد جميع الكتب
    books = Book.objects.all()

    # فلتر حسب التصنيف
    selected_category = request.GET.get('category')
    if selected_category:
        books = books.filter(category=selected_category)

    # فلتر حسب اللغة
    selected_language = request.GET.get('language')
    if selected_language:
        books = books.filter(language=selected_language)

    # فلتر حسب التقييم
    selected_rating = request.GET.get('rating')
    if selected_rating:
        books = books.filter(rating__gte=selected_rating)  # الكتب ذات التقييم أكبر من أو يساوي القيمة المحددة

    # فلتر حسب تاريخ النشر
    selected_publish_date = request.GET.get('publish_date')
    if selected_publish_date:
        books = books.filter(publish_date__lte=selected_publish_date)  # الكتب المنشورة قبل أو في التاريخ المحدد

    # الحصول على قائمة التصنيفات واللغات الفريدة
    categories = Book.objects.values_list('category', flat=True).distinct()
    languages = Book.objects.values_list('language', flat=True).distinct()

    paginator = Paginator(books, 12)  # 9 كتب في كل صفحة
    page_number = request.GET.get('page')  # الحصول على رقم الصفحة من الطلب

    try:
        books = paginator.page(page_number)  # الحصول على الكتب في الصفحة المطلوبة
    except PageNotAnInteger:
        books = paginator.page(1)  # إذا لم يكن رقم الصفحة صحيحًا، عرض الصفحة الأولى
    except EmptyPage:
        books = paginator.page(paginator.num_pages)  # إذا كانت الصفحة فارغة، عرض الصفحة الأخيرة

    return render(request, 'books.html', {
        'books': books,
        'categories': categories,
        'languages': languages,
        'selected_category': selected_category,
        'selected_language': selected_language,
        'selected_rating': selected_rating,
        'selected_publish_date': selected_publish_date,
    })




def book_detail(request, book_id):
    # استرداد الكتاب أو إظهار خطأ 404 إذا لم يتم العثور عليه
    book = get_object_or_404(Book, id=book_id)
    
    # إنشاء مفتاح فريد للجلسة بناءً على معرف الكتاب
    session_key = f'book_{book_id}_viewed'
    
    # التحقق مما إذا كان المستخدم قد شاهد الكتاب من قبل
    if not request.session.get(session_key, False):
        # زيادة عدد المشاهدات إذا لم يشاهد الكتاب من قبل
        book.views_count += 1
        book.save()
        
        # تعيين علامة في الجلسة لتجنب زيادة المشاهدات مرة أخرى
        request.session[session_key] = True
    
    return render(request, 'book_detail.html', {'book': book})