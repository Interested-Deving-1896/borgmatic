from flexmock import flexmock

import borgmatic.borg.diff
import borgmatic.borg.environment
import borgmatic.borg.feature
import borgmatic.execute
from borgmatic.borg import flags


def test_diff_calls_execute_command():
    flexmock(borgmatic.borg.feature).should_receive('available').and_return(False)
    flexmock(flags).should_receive('make_repository_flags').and_return(())
    flexmock(flags).should_receive('make_match_archives_flags').and_return(())
    flexmock(flags).should_receive('make_repository_archive_flags').and_return(())
    flexmock(borgmatic.borg.pattern).should_receive('write_patterns_file').and_return(
        flexmock(name='test')
    )
    flexmock(borgmatic.execute).should_receive('execute_command').once()
    flexmock(borgmatic.borg.environment).should_receive('make_environment').and_return({})

    borgmatic.borg.diff.diff(
        repository='repo',
        archive='archive',
        config={},
        local_borg_version=None,
        diff_arguments=flexmock(
            same_chunker_params=False,
            sort_keys=[],
            content_only=False,
            second_archive=None,
            only_patterns=False,
        ),
        global_arguments=flexmock(),
        local_path='borg',
        remote_path=None,
        patterns=[],
    )


def test_diff_with_numeric_ids_flag():
    flexmock(borgmatic.borg.feature).should_receive('available').and_return(True)
    flexmock(flags).should_receive('make_repository_flags').and_return(())
    flexmock(flags).should_receive('make_match_archives_flags').and_return(())
    flexmock(flags).should_receive('make_repository_archive_flags').and_return(())
    flexmock(borgmatic.borg.pattern).should_receive('write_patterns_file').and_return(
        flexmock(name='test')
    )
    flexmock(borgmatic.execute).should_receive('execute_command').once()
    flexmock(borgmatic.borg.environment).should_receive('make_environment').and_return({})

    borgmatic.borg.diff.diff(
        repository='repo',
        archive='archive',
        config={'numeric_ids': True},
        local_borg_version=None,
        diff_arguments=flexmock(
            same_chunker_params=False,
            sort_keys=[],
            content_only=False,
            second_archive=None,
            only_patterns=False,
        ),
        global_arguments=flexmock(),
        local_path='borg',
        remote_path=None,
        patterns=[],
    )


def test_diff_with_numeric_ids_flag_false():
    flexmock(borgmatic.borg.feature).should_receive('available').and_return(True)
    flexmock(flags).should_receive('make_repository_flags').and_return(())
    flexmock(flags).should_receive('make_match_archives_flags').and_return(())
    flexmock(flags).should_receive('make_repository_archive_flags').and_return(())
    flexmock(borgmatic.borg.pattern).should_receive('write_patterns_file').and_return(
        flexmock(name='test')
    )
    flexmock(borgmatic.execute).should_receive('execute_command').once()
    flexmock(borgmatic.borg.environment).should_receive('make_environment').and_return({})

    borgmatic.borg.diff.diff(
        repository='repo',
        archive='archive',
        config={'numeric_ids': False},
        local_borg_version=None,
        diff_arguments=flexmock(
            same_chunker_params=False,
            sort_keys=[],
            content_only=False,
            second_archive=None,
            only_patterns=False,
        ),
        global_arguments=flexmock(),
        local_path='borg',
        remote_path=None,
        patterns=[],
    )


def test_diff_with_only_patterns():
    flexmock(borgmatic.borg.feature).should_receive('available').and_return(True)
    flexmock(flags).should_receive('make_repository_flags').and_return(())
    flexmock(flags).should_receive('make_match_archives_flags').and_return(())
    flexmock(flags).should_receive('make_repository_archive_flags').and_return(())
    flexmock(borgmatic.borg.pattern).should_receive('write_patterns_file').and_return(
        flexmock(name='test')
    )
    flexmock(borgmatic.execute).should_receive('execute_command').once()
    flexmock(borgmatic.borg.environment).should_receive('make_environment').and_return({})

    borgmatic.borg.diff.diff(
        repository='repo',
        archive='archive',
        config={},
        local_borg_version=None,
        diff_arguments=flexmock(
            same_chunker_params=False,
            sort_keys=[],
            content_only=False,
            second_archive=None,
            only_patterns=True,
        ),
        global_arguments=flexmock(),
        local_path='borg',
        remote_path=None,
        patterns=[],
    )
