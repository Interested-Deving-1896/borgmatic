from flexmock import flexmock

import borgmatic.actions.diff
import borgmatic.commands.borgmatic as module


def test_run_configuration_with_diff_action_calls_run_diff():
    config = {'repositories': [{'path': 'foo'}]}
    arguments = {
        'global': flexmock(dry_run=False, monitoring_verbosity=0),
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
    flexmock(module.dispatch).should_receive('call_hooks')
    flexmock(borgmatic.actions.diff).should_receive('run_diff').once()

    list(module.run_configuration('test.yaml', config, ['/tmp/test.yaml'], arguments))


def test_run_configuration_with_diff_action_and_verbose_calls_run_diff():
    config = {'repositories': [{'path': 'foo'}]}
    arguments = {
        'global': flexmock(dry_run=False, monitoring_verbosity=1),
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

    list(module.run_configuration('test.yaml', config, ['/tmp/test.yaml'], arguments))
    config = {'repositories': [{'path': 'foo'}]}
    arguments = {
        'global': flexmock(dry_run=False, monitoring_verbosity=1),
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

    list(module.run_configuration('test.yaml', config, ['/tmp/test.yaml'], arguments))
