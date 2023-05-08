from typing import Literal, Optional
from core.database.crud.posts import PostsCRUD, Post
from core.database.models.posts import Category
from core.stores.hooks import HookStore
from core.application import storage


class PostsManager:
    def __init__(self, post_slug: Optional[str] = None, category_slug: Optional[str] = None, queryset: Optional[str] = None) -> None:
        """
        Post manager used to get multiple or single post
        """
        self.post_slug = post_slug
        self.category_slug = category_slug
        self.queryset = queryset

    def get(self, limit: Optional[int]):
        if self.post_slug:
            hook = self.hook_single_post()

            if hook:
                return hook.execute(Post, slug=self.post_slug)
            
            query = PostsCRUD.get_post(self.post_slug)
            return query

        if self.category_slug:
            hook = self.hook_category_post()

            if hook:
                return hook.execute(Post, Category, slug=self.category_slug)
            query = PostsCRUD.get_category_posts(self.category_slug)
            return query
        
        hook = self.hook_multiple_posts()

        if hook:
            return hook.execute(Post)

        query = PostsCRUD.get_posts(limit)
        return query
    
    def hook_single_post(self):
        hooks_store: HookStore = storage.dispatch("hooks")
        hook = hooks_store.get_hook("get_post")

        return hook
    
    def hook_multiple_posts(self):
        hooks_store: HookStore = storage.dispatch("hooks")
        hook = hooks_store.get_hook("get_posts")

        return hook
    
    def hook_category_posts(self):
        hooks_store: HookStore = storage.dispatch("hooks")
        hook = hooks_store.get_hook("get_category_posts")

        return hook