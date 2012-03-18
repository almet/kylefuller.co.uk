Title: Pre-populating data in the admin panel
Slug: pre-populating-data-admin-panel
Category: Django
Tags: Django
Date: 2009-07-01

I have always found it awkward working with sites and user's in django admin panel. James Bennet from [b-list.org](http://www.b-list.org/weblog/2008/dec/24/admin/) explained his way of doing it on his blog, but I found his way a bit limiting, I still want superusers to be able to change the author of a post.

After looking around in the source code for `ModelAdmin` I found two method's, one of which was not documented. These were `formfield_for_manytomany` and `formfield_for_foreignkey`. These methods allow us to supply our own FormField, which could have initial data. These methods also get passed the `HttpRequest`, which contains the user. So we can fill in author of a blog post and the current site.

In this post I will quickly show you how to use this method to fill in current data based upon the request inside the admin.

### My model

Here is a model from which the rest of the article will work from.

    :::python
    from django.db import models
    from django.contrib.sites.models import Site
    from django.contrib.auth.models import User

    class Post(models.Model):
        title = models.CharField(max_length=255)
        content = models.TextField(blank=True)

        sites = models.ManyToManyField(Site)
        author = models.ForeignKey(User)

As you can see, the author is a ForeignKey field, and sites is a ManyToMany field. The methods we use to set the default reflects this. We use `formfield_for_foreignkey` to set the default user.

### Here is my ModelAdmin class

    :::python
    class PostAdmin(admin.ModelAdmin):
        fieldsets = (
        (None, {
            'fields': ('title', 'content',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('author', 'sites',)
        })
    )

    admin.site.register(Post, PostAdmin)

### Selecting the current site

To select the current site, what we will do is create a method called `formfield_for_manytomany` inside our `PostAdmin` class. This method will be called each time the admin panel goes to draw a `ManyToMany` field in a Post. So all we do is set the initial value to the current site. But it is important to remember that the field may be something else, so it is important to check if it is the sites field.

    :::python
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'sites':
            kwargs['initial'] = [Site.objects.get_current()]
            return db_field.formfield(**kwargs)

        return super(PostAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

### Selecting the current user

This is very similar to selecting the current site, instead we create a method called `formfield_for_foreignkey` for ForeignKey's instead of `ManyToMany` fields.

    :::python
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)

        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

Now that we have selected the current user, it would be nice to only let superusers use this field, but I couldn't find a way to only show this for certain users. So instead we will just disallow normal user's from saving the post as another user.

I dont think it is possible to optionally hide the author field from a user, so what I have done was to disallow a non superuser from editing the post's author.

#### Disallowing a user from changing another post

    :::python
    def has_change_permission(self, request, obj=None):
        has_class_permission = super(PostAdmin, self).has_change_permission(request, obj)

        if not has_class_permission:
            return False

        if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
            return False

This snippet was not written by myself, but by James Bennet from [b-list.org](http://www.b-list.org/weblog/2008/dec/24/admin/).

### Only let the user view their own posts

Another measure to limit the possibilities of the user can be to let the user only view their own posts. To do this we just change the queryset to filter posts where the author is themselves. We still want superusers to see all posts, so only filter it for normal users.

    :::python
    def queryset(self, request):
        if request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(author=request.user)

To see a complete example of this you can view the source code for [lithium](https://github.com/kylef/lithium).
