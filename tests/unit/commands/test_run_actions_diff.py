from flexmock import flexmock

import borgmatic.actions.diff
import borgmatic.commands.borgmatic as module


def test_run_actions_with_diff_calls_diff_action():
    config = {'repositories': [{'path': 'foo'}]}
    arguments = {
        'global': flexmock(dry_run=False),
        'diff': flexmock(
            archive='archive1',
            same_chunker_params=False,
            sort_by=None,
            sort_keys=[],
            content_only=False,
            second_archive=None,
            only_patterns=False,
        ),
    }
    flexmock(module.borg_version).should_receive('local_borg_version').and_return(flexmock())
    flexmock(borgmatic.actions.diff).should_receive('run_diff').once()

    list(
        module.run_actions(
            arguments=arguments,
            config_filename='test.yaml',
            config=config,
            config_paths=[],
            local_path=None,
            remote_path=None,
            local_borg_version=None,
            repository={'path': 'foo'},
        )
    )


def test_run_actions_with_diff_and_dry_run_calls_diff_action():
    config = {'repositories': [{'path': 'foo'}]}
    arguments = {
        'global': flexmock(dry_run=True),
        'diff': flexmock(
            archive='archive1',
            same_chunker_params=False,
            sort_by=None,
            sort_keys=[],
            content_only=False,
            second_archive=None,
            only_patterns=False,
        ),
    }
    flexmock(module.borg_version).should_receive('local_borg_version').and_return(flexmock())
    flexmock(borgmatic.actions.diff).should_receive('run_diff').once()

    list(
        module.run_actions(
            arguments=arguments,
            config_filename='test.yaml',
            config=config,
            config_paths=[],
            local_path=None,
            remote_path=None,
            local_borg_version=None,
            repository={'path': 'foo'},
        )
    )
