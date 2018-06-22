# logs/urls.py
from django.urls import path

from . import views


app_name = "logs"

urlpatterns = [

    # # # # # トップページ # # # # #

    # ex: /logs/top/
    path("top/",
        views.TopView.as_view(),
        name="top"
    ),

    # # # # # Event モデル # # # # #

    # かんたん登録
    # ex:/logs/events/easy/
    path("events/easy/",
        views.EventTopView.as_view(),
        name="event-top"
    ),

    # イベント一覧
    # ex: /logs/events/
    path("events/",
        views.EventIndexView.as_view(),
        name="event-index"
    ),

    # イベントを作成する
    # ex: /logs/events/new/
    path("events/new/",
        views.EventCreateView.as_view(),
        name="event-new"
    ),

    # イベントを編集する
    # ex: /logs/events/edit/01CBAW.../
    path("events/edit/<str:pk>/",
        views.EventEditView.as_view(),
        name="event-edit"
    ),

    # # # # # Timestamp モデル # # # # #

    # タイムスタンプ一覧
    # ex: /logs/timestamps/
    path("timestamps/",
        views.TimestampIndexView.as_view(),
        name="timestamp-index"
    ),

    # タイムスタンプを作成する
    # ex: /logs/timestamps/new/
    path("timestamps/new/",
        views.TimestampCreateView.as_view(),
        name="timestamp-new"
    ),

    # タイムスタンプを作成する(トップページのかんたん登録から)
    # ex: /logs/timestamps/new/01CBAW.../
    path("timestamps/new/<str:event_id>/",
        views.timestamp_new,
        name="timestamp-new-top"
    ),

    # タイムスタンプを編集する
    # ex: /logs/timestamps/edit/01CBAW.../
    path("timestamps/edit/<str:pk>/",
        views.TimestampEditView.as_view(),
        name="timestamp-edit"
    ),

    # # # # # Theme モデル # # # # #

    # タイムスタンプのテーマ一覧
    # ex: /logs/themes/
    path("themes/",
        views.ThemeIndexView.as_view(),
        name="theme-index"
    ),

    # タイムスタンプのテーマの新規登録
    # ex: /logs/themes/new/
    path("themes/new/",
        views.ThemeCreateView.as_view(),
        name="theme-new"
    ),

    # タイムスタンプのテーマの編集
    # ex: /logs/themes/edit/01CBAW.../
    path("themes/edit/<str:pk>/",
        views.ThemeEditView.as_view(),
        name="theme-edit"
    ),

    # # # # # PDC モデル # # # # #

    # PDC 一覧
    # ex: /logs/pdcs/
    path("pdcs/",
        views.PDCIndexView.as_view(),
        name="pdc-index"
    ),

    # PDC の新規登録
    # ex: /logs/pdcs/new/
    path("pdcs/new/",
        views.PDCCreateView.as_view(),
        name="pdc-new"
    ),

    # PDC の編集   
    # ex: /logs/pdcs/edit/01CBAW.../
    path("pdcs/edit/<str:pk>/",
        views.PDCEditView.as_view(),
        name="pdc-edit"
    ),

    # 実行済み PDC の一覧
    # ex: /logs/pdcs_done/
    path("pdcs_done/",
        views.PDCDoneIndexView.as_view(),
        name="pdc-done-index"
    ),

    # # # # # Weather モデル # # # # #

    # 気象データ一覧
    # ex: /logs/weather/
    path("weather/",
        views.WeatherIndexView.as_view(),
        name="weather-index"
    ),

    # 気象データの新規登録
    # ex: /logs/weather/new/
    path("weather/new/",
        views.WeatherCreateView.as_view(),
        name="weather-new"
    ),

    # 気象データの編集
    # ex: /logs/weather/edit/01CBAW.../
    path("weather/edit/<str:pk>/",
        views.WeatherEditView.as_view(),
        name="weather-edit"
    ),

    # # # # # ツール類 # # # # #

    # ツール一覧
    # ex: /logs/tools/
    path("tools/",
        views.ToolsTemplateView.as_view(),
        name="tools"
    ),

    # ブログを書く
    # ex: /logs/tools/blog/
    path("tools/blog/",
        views.BlogTemplateView.as_view(),
        name="tools-blog"
    ),

    # 理解度をチェックする
    # ex: /logs/tools/comprehension/
    path("tools/comprehension/",
        views.ComprehensionTemplateView.as_view(),
        name="tools-comprehension"
    ),

    # ヤル気が出ない時
    # ex: /logs/tools/motivation/
    path("tools/motivation/",
        views.MotivationTemplateView.as_view(),
        name="tools-motivation"
    ),

    # 品質を安定させる (作業前)
    # ex: /logs/tools/quality_check/
    path("tools/quality_check/",
        views.QualityCheckTemplateView.as_view(),
        name="tools-quality-check"
    ),

    # 品質を安定させる (作業後)
    # ex: /logs/tools/quality_check_after/
    path("tools/quality_check_after/",
        views.QualityCheckAfterTemplateView.as_view(),
        name="tools-quality-check-after"
    ),

    # アリス
    # ex: /logs/tools/alice/
    path("tools/alice/",
        views.AliceInWonderlandView.as_view(),
        name="tools-alice"
    ),

    # 設定
    # ex: /logs/tools/settings/
    path("tools/settings/",
        views.SettingsTemplateView.as_view(),
        name="tools-settings"
    ),

    # 練習用ページ
    # ex: /logs/tools/settings/exercise/
    path("tools/settings/exercise/",
        views.ExerciseTemplateView.as_view(),
        name="tools-settings-exercise"
    ),

    # ライブラリ
    # ex: /logs/libraries/
    path("libraries/",
        views.LibrariesTemplateView.as_view(),
        name="libraries"
    ),

    # リスニング (一覧)
    # ex: /logs/libraries/listening/
    path("libraries/listening/",
        views.ListeningTemplateView.as_view(),
        name="libraries-listening"
    ),

    # # # # # LogTitle モデル # # # # #

    # ログタイトルの一覧
    # ex: /logs/log_titles/
    path("log_titles/",
        views.LogTitleIndexView.as_view(),
        name="log-title-index"
    ),

    # ログタイトルの新規登録
    # ex: /logs/log_titles/new/
    path("log_titles/new/",
        views.LogTitleCreateView.as_view(),
        name="log-title-new"
    ),

    # ログタイトルの編集
    # ex: /logs/log_titles/edit/01CBAW.../
    path("log_titles/edit/<str:pk>/",
        views.LogTitleEditView.as_view(),
        name="log-title-edit"
    ),

    # # # # # Log モデル # # # # #

    # ログの一覧
    # ex: /logs/logs/
    path("logs/",
        views.LogIndexView.as_view(),
        name="log-index"
    ),

    # ログの新規登録
    # ex: /logs/logs/new/
    path("logs/new/",
        views.LogCreateView.as_view(),
        name="log-new"
    ),

    # ログの編集
    # ex: /logs/logs/edit/01CBAW.../
    path("logs/edit/<str:pk>/",
        views.LogEditView.as_view(),
        name="log-edit"
    ),

    # 睡眠ログの取得 (JSONデータ)
    # ex: /logs/logs/sleep_index.json/
    path("logs/sleep_index.json/",
        views.sleep_index_json,
        name="sleep-index-json"
    ),

    # 睡眠テーブルの表示
    # ex: /logs/logs/sleep_index_tabulate/
    path("logs/sleep_index_tabulate/",
        views.SleepIndexTabulateView.as_view(),
        name="sleep-index-tabulate"
    ),

    # # # # # Proverb モデル # # # # #

    # 名言/格言一覧
    # ex: /logs/proverbs/
    path("proverbs/",
        views.ProverbIndexView.as_view(),
        name="proverb-index"
    ),

    # 名言/格言の詳細 (ランダムに選択)
    # ex: /logs/proverbs/
    path("proverbs/detail/",
        views.proverb_detail_random,
        name="proverb-detail"
    ),

    # 名言/格言の新規登録
    # ex: /logs/proverbs/new/
    path("proverbs/new/",
        views.ProverbCreateView.as_view(),
        name="proverb-new"
    ),

    # 名言/格言の編集
    # ex: /logs/proverbs/edit/01CBAW.../
    path("proverbs/edit/<str:pk>/",
        views.ProverbEditView.as_view(),
        name="proverb-edit"
    ),

    # # # # # Routine モデル # # # # #

    # ルーチンの一覧
    # ex: /logs/routines/
    path("routines/",
        views.RoutineIndexView.as_view(),
        name="routine-index"
    ),

    # ルーチンの新規登録
    # ex: /logs/routines/new/
    path("routines/new/",
        views.RoutineCreateView.as_view(),
        name="routine-new"
    ),

    # ルーチンの編集
    # ex: /logs/routines/edit/01CBAW.../
    path("routines/edit/<str:pk>/",
        views.RoutineEditView.as_view(),
        name="routine-edit"
    ),

    # # # # # RoutineStamp モデル # # # # #

    # ルーチンスタンプの一覧
    # ex: /logs/routinestamps/
    path("routinestamps/",
        views.RoutineStampIndexView.as_view(),
        name="routinestamp-index"
    ),

    # ルーチンスタンプのテーブル表示
    # ex: /logs/routinestamps/tabulate/
    path("routinestamps/tabulate/",
        views.routinestamps_tabulate,
        name="routinestamp-tabulate"
    ),

    # ルーチンスタンプの新規登録
    # ex: /logs/routinestamps/new/
    path("routinestamps/new/",
        views.RoutineStampCreateView.as_view(),
        name="routinestamp-new"
    ),

    # ルーチンスタンプの編集
    # ex: /logs/routinestamps/edit/01CBAW.../
    path("routinestamps/edit/<str:pk>/",
        views.RoutineStampEditView.as_view(),
        name="routinestamp-edit"
    ),

    # # # # # Genre モデル # # # # #

    # ノートのジャンル一覧
    # ex: /logs/genre/
    path("genre/",
        views.GenreIndexView.as_view(),
        name="genre-index"
    ),

    # ノートのジャンルの新規作成
    # ex: /logs/genre/new/
    path("genre/new/",
        views.GenreCreateView.as_view(),
        name="genre-new"
    ),

    # ノートのジャンルの新規作成
    # ex: /logs/genre/edit/01CBAW.../
    path("genre/edit/<str:pk>/",
        views.GenreEditView.as_view(),
        name="genre-edit"
    ),

    # # # # # Note モデル # # # # #

    # ノートの一覧
    # ex: /logs/notes/
    path("notes/",
        views.NoteIndexView.as_view(),
        name="note-index"
    ),

    # ノートの詳細
    # ex: /logs/notes/01CBAW.../detail/42/
    path("notes/<str:pk>/detail/<int:page_number>/",
        views.NoteDetailView.as_view(),
        name="note-detail"
    ),

    # ノートの新規作成
    # ex: /logs/notes/new/
    path("notes/new/",
        views.NoteCreateView.as_view(),
        name="note-new"
    ),

    # ノートの新規編集
    # ex: /logs/notes/edit/01CBAW.../
    path("notes/edit/<str:pk>/",
        views.NoteEditView.as_view(),
        name="note-edit"
    ),

    # # # # # Concern モデル # # # # #

    # 関心事の一覧
    # ex: /logs/concerns/
    path("concerns/",
        views.ConcernIndexView.as_view(),
        name="concern-index"
    ),

    # 関心事の詳細
    # ex: /logs/concerns/01CBAW.../detail/
    path("concerns/<str:pk>/detail/",
        views.ConcernDetailView.as_view(),
        name="concern-detail"
    ),

    # 関心事の詳細 ( 接続情報を JSON データで得る )
    # ex: /logs/concerns/01CBAW.json/
    path("concerns/<str:pk>.json/",
        views.concern_detail_json,
        name="concern-detail-json"
    ),

    # 関心事の新規登録
    # ex: /logs/concerns/new/
    path("concerns/new/",
        views.ConcernCreateView.as_view(),
        name="concern-new"
    ),

    # 関心事の編集
    # ex: /logs/concerns/edit/01CBAW.../
    path("concerns/edit/<str:pk>/",
        views.ConcernEditView.as_view(),
        name="concern-edit"
    ),

    # ノードの新規作成 ( ルートに直接接続するノード )
    # ex: /logs/concerns/01CBAW.../nodes/new_to_root/
    path("concerns/<str:concern_id>/nodes/new_to_root/",
        views.NodeToRootCreateView.as_view(),
        name="node-new-to-root"
    ),

    # ノードの編集
    # ex: /logs/concerns/42/nodes/edit/42/
    path("concerns/<str:concern_id>/nodes/edit/<str:pk>/",
        views.NodeEditView.as_view(),
        name="node-edit"
    ),

    # 接続元ノードの作成
    # ex: /logs/concerns/42/nodes/42/new_source/
    path("concerns/<str:concern_id>/nodes/<str:target_id>/new_source/",
        views.SourceNodeCreateView.as_view(),
        name="node-new-source"
    ),

    # 接続先ノードの作成
    # ex: /logs/concerns/42/nodes/42/new_target/
    path("concerns/<str:concern_id>/nodes/<str:source_id>/new_target/",
        views.TargetNodeCreateView.as_view(),
        name="node-new-target"
    ),

]