from flexmock import flexmock

import borgmatic.actions.diff
import borgmatic.actions.pattern
import borgmatic.borg.diff
import borgmatic.borg.repo_list


def test_run_diff_calls_borg_diff():
    flexmock(borgmatic.actions.pattern).should_receive('process_patterns').and_return([])
    flexmock(borgmatic.borg.repo_list).should_receive('resolve_archive_name').and_return('archive')
    flexmock(borgmatic.borg.diff).should_receive('diff').once()

    borgmatic.actions.diff.run_diff(
        repository={'path': 'repo'},
        config={},
        local_borg_version=None,
        diff_arguments=flexmock(
            archive='archive',
            same_chunker_params=False,
            sort_by=None,
            sort_keys=[],
            content_only=False,
            second_archive=None,
            only_patterns=False,
        ),
        global_arguments=flexmock(),
        local_path=None,
        remote_path=None,
    )
