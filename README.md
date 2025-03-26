## auth
- 로그인 기능 
- user 
    - username
    - passward
    - name

- Post (유저가 작성하는 게시글) : 유저에 속함.
    - UniqueID
    - title
    - content 
    - user_id (ForeignKey) : 부모와 연결해줌

- => 1:N 관계 (한사람이 여러개의 게시글을 작성함.)

- Comment
    - UniqueID
    - content
    - user_id
    - post_id

- => 1:N 관계 (로그인 - 게시글 - 댓글 )