import sublime, sublime_plugin, re

class FillControllerCommand(sublime_plugin.TextCommand):
    def run(self, edit, user_input=None):
        self.view.insert(edit, 0, "<?php\nsf_controller");
        self.view.run_command('auto_complete');

class FillEntityCommand(sublime_plugin.TextCommand):
    def run(self, edit, user_input=None):
        self.view.insert(edit, 0, "<?php\nsf_entity");
        self.view.run_command('auto_complete');

class FillDataFixtureCommand(sublime_plugin.TextCommand):
    def run(self, edit, user_input=None):
        self.view.insert(edit, 0, "<?php\nsf_data_fixture");
        self.view.run_command('auto_complete');

class FillFormTypeCommand(sublime_plugin.TextCommand):
    def run(self, edit, user_input=None):
        self.view.insert(edit, 0, "<?php\nsf_form");
        self.view.run_command('auto_complete');

class FillFormDataTransformerCommand(sublime_plugin.TextCommand):
    def run(self, edit, user_input=None):
        self.view.insert(edit, 0, "<?php\nsf_form");
        self.view.run_command('auto_complete');

class FillRepositoryCommand(sublime_plugin.TextCommand):
    def run(self, edit, user_input=None):
        self.view.insert(edit, 0, "<?php\nsf_repo");
        self.view.run_command('auto_complete');

class FillTestsCommand(sublime_plugin.TextCommand):
    def run(self, edit, user_input=None):
        self.view.insert(edit, 0, "<?php\nsf_tests");
        self.view.run_command('auto_complete');

class SymfonyComplexListener(sublime_plugin.EventListener):

    def on_load(self, view):
        syntax   = ''
        fileName = view.file_name();

        isController          = False
        isEntity              = False
        isDataFixture         = False
        isFormType            = False
        isFormDataTransformer = False
        isRepository          = False
        isTests               = False

        # XML Services - DONE
        if re.compile('services\.xml$').search(fileName):
            syntax = 'Packages/SymfonyComplex/SymfonyServicesXml.tmLanguage';
            view.settings().set('syntax', syntax)

        # XML Routing
        if re.compile('routing\.xml$').search(fileName):
            syntax = 'Packages/SymfonyComplex/SymfonyRoutingXml.tmLanguage';
            view.settings().set('syntax', syntax)

        if not re.compile('\.php$').search(fileName):
            return;

        # Entity - Done
        if re.compile('\/Entity\/').search(fileName):
            syntax = 'Packages/SymfonyComplex/DoctrineEntity.tmLanguage';
            isEntity = True

        # Repository - Done
        if re.compile('\/Repository\/').search(fileName) or re.compile('Repository\.php$').search(fileName):
            syntax = 'Packages/SymfonyComplex/DoctrineRepository.tmLanguage';
            isRepository = True

        # DataFixtures - Done
        if re.compile('\/DataFixtures\/ORM\/').search(fileName):
            syntax = 'Packages/SymfonyComplex/DoctrineDataFixtures.tmLanguage';
            isDataFixture = True

        # Controller - Done
        if re.compile('Controller\.php$').search(fileName):
            syntax = 'Packages/SymfonyComplex/SymfonyController.tmLanguage';
            isController = True

        # Form Type - Done
        if re.compile('\/Form\/Type\/').search(fileName) or re.compile('FormType\.php$').search(fileName):
            syntax = 'Packages/SymfonyComplex/SymfonyFormType.tmLanguage';
            isFormType = True

        # Form DataTransformer - Done
        if re.compile('\/Form\/DataTransformer\/').search(fileName):
            syntax = 'Packages/SymfonyComplex/SymfonyFormDataTransformer.tmLanguage';
            isFormDataTransformer = True

        # Tests
        if re.compile('\/Tests\/').search(fileName):
            syntax = 'Packages/SymfonyComplex/SymfonyTests.tmLanguage';
            isTests = True

        # TwigExtension
        if re.compile('\/Twig\/').search(fileName) and re.compile('Extension\.php$').search(fileName):
            syntax = 'Packages/SymfonyComplex/TwigExtension.tmLanguage';

        print("syntax: " + syntax)
        view.settings().set('syntax', syntax)

        if view.size():
            return

        if isController:
            view.run_command('fill_controller');

        if isEntity:
            view.run_command('fill_entity');

        if isDataFixture:
            view.run_command('fill_data_fixture');

        if isFormType:
            view.run_command('fill_form_type');

        if isFormDataTransformer:
            view.run_command('fill_form_data_transformer');

        if isRepository:
            view.run_command('fill_repository');

        if isTests:
            view.run_command('fill_tests');
