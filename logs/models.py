from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,\
BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator,\
MaxValueValidator
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import ulid


# Create your models here.
class ULIDField(models.CharField):
    """ULIDを使用したフィールド"""

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 26
        super(ULIDField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return "char(26)"


class TimestampedModel(models.Model):
    """作成時/更新時を記録する抽象クラス"""

    # ID (主キー: ULIDを使用)
    id = ULIDField(
        default=ulid.new,
        primary_key=True,
        editable=False
    )

    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)

    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """ユーザーマネージャー"""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル"""

    # ID (主キー: ULIDを使用)
    id = ULIDField(
        default=ulid.new,
        primary_key=True,
        editable=False
    )

    # メールアドレス
    email = models.EmailField(
        _("email address"),
        unique=True
    )

    # 名
    first_name = models.CharField(
        _("first name"),
        max_length=30,
        blank=True
    )

    # 姓
    last_name = models.CharField(
        _("last name"),
        max_length=30,
        blank=True
    )

    # 開発者かどうか
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        )
    )

    # 現在使用中のアカウントか
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        )
    )

    # 追加日
    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now
    )

    # マネージャークラス
    objects = UserManager()

    # フィールド
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    # 他にもメソッドが続くが..


# # # # # Event モデル # # # # #
class Event(TimestampedModel):
    """イベント(タイムスタンプで使用する)"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # イベント名
    name = models.CharField(
        max_length=40,
        verbose_name=_("event name")
    )

    def __str__(self):
        return "%s" % self.name


# # # # # Timestamp モデル # # # # #
class Timestamp(TimestampedModel):
    """タイムスタンプ(事象の発生時刻を記録)"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user")
    )

    # イベントの種類
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name=_("event")
    )

    # 事象の発生時刻
    at = models.DateTimeField(
        blank=True
    )

    def __str__(self):
        return "%s at %s" % (
            self.event,    # ※余分なクエリが発生しそうな部分@180417
            self.at,
        )


# # # # # Theme モデル # # # # #
class Theme(TimestampedModel):
    """PDCAサイクルのテーマ"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user")
    )

    # タイトル
    title = models.CharField(
        max_length=40,
        verbose_name=_("title")
    )

    def __str__(self):
        return "%s" % self.title


# # # # # PDC モデル # # # # #
class PDC(TimestampedModel):

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user")
    )

    # テーマ
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE,
        verbose_name=_("theme")
    )

    # Plan
    plan = models.CharField(
        max_length=64,
        verbose_name=_("plan")
    )

    # Is done
    is_done = models.BooleanField(
        default=False,
        verbose_name=_("is done")
    )

    # Check
    check = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("check")
    )

    def percentage(self):
        """Checkデータが200文字中何%まで記録されているか"""
        length = len(self.check)
        max_length = 200
        return round(length / max_length * 100, 1)


# # # # # Weather モデル # # # # #
class Weather(TimestampedModel):
    """一日の気象データ"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="ユーザー"
    )

    # 日付
    date = models.DateField(
        verbose_name="年/月/日"
    )

    # 最高気温
    temperature_highest = models.SmallIntegerField(
        validators=(
            MinValueValidator(-10),
            MaxValueValidator(45),
        ),
        verbose_name="最高気温(℃)"
    )

    # 最低気温
    temperature_lowest = models.SmallIntegerField(
        validators=(
            MinValueValidator(-20),
            MaxValueValidator(35),
        ),
        verbose_name="最低気温(℃)"
    )

    # 降水確率 (%)
    # ( 正式には Probability of precipitation という )
    rainy_percent = models.SmallIntegerField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(100),
        ),
        verbose_name="降水確率(%)"
    )


# # # # # LogTitle モデル # # # # #
class LogTitle(TimestampedModel):
    """ログのタイトル"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # タイトル
    title = models.CharField(
        max_length=20,
        verbose_name="タイトル"
    )

    def __str__(self):
        return "%s" % self.title


# # # # # Log モデル # # # # #
class Log(TimestampedModel):
    """開始時刻と終了時刻を持つログ"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # タイトル
    title = models.ForeignKey(
        LogTitle,
        on_delete=models.CASCADE
    )

    # 開始時刻
    start = models.DateTimeField(
    )

    # 終了時刻
    finish = models.DateTimeField(
    )


# # # # # Proverb モデル # # # # #
class Proverb(TimestampedModel):
    """名言/格言"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # 本文
    content = models.CharField(
        max_length=200,
        verbose_name="名言/格言"
    )

    def first_message(self):
        """最初の一文を取得する"""
        i = self.content.find("。")
        return self.content[:i+1]

    def remaining_messages(self):
        """最初の一文より後のメッセージを取得する"""
        content = self.content
        i = content.find("。")
        return content[i+1:]


# # # # # Routine モデル # # # # #
class Routine(TimestampedModel):
    """ルーチン項目"""

    # ※後からルーチンの順序を変更できるようにしたいのだが..
    # →

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="ユーザー"
    )

    # ソート用のオーダー
    order = models.SmallIntegerField(
        verbose_name="オーダー番号"
    )

    # 項目名
    name = models.CharField(
        max_length=20,
        verbose_name="ルーチン名"
    )

    def __str__(self):
        return "%s" % self.name


class RoutineStamp(TimestampedModel):
    """ルーチン実行の登録用スタンプ"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="ユーザー"
    )

    # ルーチン
    routine = models.ForeignKey(
        Routine,
        on_delete=models.CASCADE,
        verbose_name="ルーチン"
    )

    # 実行日時
    at = models.DateTimeField(
        verbose_name="実行日時"
    )


# # # # # Genre モデル # # # # #
class Genre(TimestampedModel):
    """ノートのジャンル"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="ユーザー"
    )

    # ジャンル名
    name = models.CharField(
        max_length=20,
        null=False,
        verbose_name="ジャンル名"
    )

    # 言語名
    language = models.CharField(
        max_length=20,
        null=False,
        verbose_name="言語"
    )

    def __str__(self):
        return "%s" % self.name


# # # # # Note モデル # # # # #
class Note(TimestampedModel):
    """ノート"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="ユーザー"
    )

    # ジャンル
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name="ジャンル"
    )

    # タイトル
    title = models.CharField(
        max_length=32,
        null=False,
        verbose_name="タイトル"
    )

    # コード
    code = models.TextField(
        null=False,
        verbose_name="コード"
    )

    # 復習 1 回目
    is_reviewed_1 = models.BooleanField(
        default=False,
        null=False,
        verbose_name="復習1回目"
    )

    # 復習 2 回目
    is_reviewed_2 = models.BooleanField(
        default=False,
        null=False,
        verbose_name="復習2回目"
    )

    # 復習 3 回目
    is_reviewed_3 = models.BooleanField(
        default=False,
        null=False,
        verbose_name="復習3回目"
    )

    # 復習 4 回目
    is_reviewed_4 = models.BooleanField(
        default=False,
        null=False,
        verbose_name="復習4回目"
    )

    # 復習 5 回目
    is_reviewed_5 = models.BooleanField(
        default=False,
        null=False,
        verbose_name="復習5回目"
    )

    def __str__(self):
        return "%s" % self.title

    def percentage(self):
        """何回目まで復習できているかを%で得る"""
        if not self.is_reviewed_1:
            return 0.0
        elif not self.is_reviewed_2:
            return 20.0
        elif not self.is_reviewed_3:
            return 40.0
        elif not self.is_reviewed_4:
            return 60.0
        elif not self.is_reviewed_5:
            return 80.0
        return 100.0

    def days_elapsed(self):
        """ノート作成日時からの経過日数を取得する"""
        return (timezone.now() - self.created_at).days


# # # # # Concern モデル # # # # #
class Concern(TimestampedModel):
    """関心事"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # 内容
    content = models.CharField(
        max_length=40
    )

    # 関心事のタイプ
    # 0 .. なぜなぜ分析
    # 1 .. 目標設定
    ANALYZE = 0
    SET_TARGET = 1
    NODE_TYPES = (
        (ANALYZE, "なぜなぜ分析"),
        (SET_TARGET, "目標設定")
    )

    concern_type = models.IntegerField(
        choices=NODE_TYPES
    )

    def __str__(self):
        return "%s" % self.content


# # # # # Node モデル # # # # #
class Node(TimestampedModel):
    """mind-graphのノード"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # 関心事
    concern = models.ForeignKey(
        Concern,
        on_delete=models.CASCADE
    )

    # 自身から接続しているノード
    targets = models.ManyToManyField(
        "self",
        related_name="sources",    # 逆参照する場合の名前
        symmetrical=False,
        blank=True
    )

    # 内容
    content = models.CharField(
        max_length=40
    )

    # ルートに直接接続するかどうか
    to_root = models.BooleanField(
        default=False
    )

    # ノードタイプ
    NORMAL = 0
    REVERSE = 1
    NODE_TYPES = (
        (NORMAL, "ノーマル"),
        (REVERSE, "反論"),
    )
    node_type = models.IntegerField(
        choices=NODE_TYPES,
        default=NORMAL
    )

    def __str__(self):
        return "%s" % self.content