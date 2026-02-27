import logging

from flexmock import flexmock

from borgmatic.borg import diff as module


def test_diff_calls_execute_command():
    flexmock(module.borgmatic.borg.feature).should_receive('available').and_return(False)
    flexmock(module.borgmatic.borg.flags).should_receive('make_repository_flags').and_return(())
    flexmock(module.borgmatic.borg.flags).should_receive('make_match_archives_flags').and_return(())
    flexmock(module.borgmatic.borg.flags).should_receive(
        'make_repository_archive_flags'
    ).and_return(())
    flexmock(module.borgmatic.borg.pattern).should_receive('write_patterns_file').and_return(
        flexmock(name='test')
    )
    flexmock(module.borgmatic.execute).should_receive('execute_command').once()
    flexmock(module.borgmatic.borg.environment).should_receive('make_environment').and_return({})

    module.borgmatic.borg.diff.diff(
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
    flexmock(module.borgmatic.borg.feature).should_receive('available').and_return(True)
    flexmock(module.borgmatic.borg.flags).should_receive('make_repository_flags').and_return(())
    flexmock(module.borgmatic.borg.flags).should_receive('make_match_archives_flags').and_return(())
    flexmock(module.borgmatic.borg.flags).should_receive(
        'make_repository_archive_flags'
    ).and_return(())
    flexmock(module.borgmatic.borg.pattern).should_receive('write_patterns_file').and_return(
        flexmock(name='test')
    )
    flexmock(module.borgmatic.execute).should_receive('execute_command').once()
    flexmock(module.borgmatic.borg.environment).should_receive('make_environment').and_return({})

    module.borgmatic.borg.diff.diff(
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
    flexmock(module.borgmatic.borg.feature).should_receive('available').and_return(True)
    flexmock(module.borgmatic.borg.flags).should_receive('make_repository_flags').and_return(())
    flexmock(module.borgmatic.borg.flags).should_receive('make_match_archives_flags').and_return(())
    flexmock(module.borgmatic.borg.flags).should_receive(
        'make_repository_archive_flags'
    ).and_return(())
    flexmock(module.borgmatic.borg.pattern).should_receive('write_patterns_file').and_return(
        flexmock(name='test')
    )
    flexmock(module.borgmatic.execute).should_receive('execute_command').once()
    flexmock(module.borgmatic.borg.environment).should_receive('make_environment').and_return({})

    module.borgmatic.borg.diff.diff(
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
    # Mock the feature check
    flexmock(module.borgmatic.borg.feature).should_receive('available').and_return(True)

    flexmock(module.borgmatic.borg.flags).should_receive('make_repository_flags').and_return(
        ('--repo', 'repo')
    )
    flexmock(module.borgmatic.borg.flags).should_receive('make_match_archives_flags').and_return(())
    flexmock(module.borgmatic.borg.flags).should_receive(
        'make_repository_archive_flags'
    ).and_return(())

    environment = flexmock()
    flexmock(module.borgmatic.borg.environment).should_receive('make_environment').and_return(
        environment
    )

    flexmock(module.borgmatic.borg.pattern).should_receive('write_patterns_file').and_return(
        '/tmp/test_patterns'
    )

    expected_command = (
        'borg',
        'diff',
        '--log-json',  # Add this flag
        '--repo',
        'repo',
        None,
    )

    flexmock(module.borgmatic.execute).should_receive('execute_command').with_args(
        full_command=expected_command,
        output_log_level=logging.ANSWER,
        environment=environment,
        working_directory=None,
        borg_local_path='borg',
        borg_exit_codes=None,
    ).once()

    module.borgmatic.borg.diff.diff(
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
